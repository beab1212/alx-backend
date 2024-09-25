import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';
import express from 'express';

const client = createClient();
const queue = createQueue();
const app = express();
let reservationIsSet = false;

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

function reserveSeat(number) {
  return client.SET('available_seats', number);
}

function getCurrentAvailableSeats() {
  const GET = promisify(client.GET).bind(client);
  return GET('available_seats');
}

app.get('/available_seats', (req, res) => {
  getCurrentAvailableSeats()
    .then((seats) => {
      res.json({ numberOfAvailableSeats: seats });
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json(null);
    });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats -= 1;
    reserveSeat(availableSeats);
    if (availableSeats >= 0) {
      if (availableSeats === 0) reservationIsSet = false;
      done();
    }
    done(new Error('Not enough seats available'));
  });
});

app.get('/reserve_seat', (req, res) => {
  if (reservationIsSet === false) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat', { task: 'reserve a seat' });
  job
    .on('complete', (status) => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err.message || err.toString()}`);
    })
    .save((err) => {
      if (err) return res.json({ status: 'Reservation failed' });
      return res.json({ status: 'Reservation in process' });
    });
});

app.listen(1245, () => {
  reserveSeat(50);
  reservationIsSet = true;
  console.log('API available on localhost via port 1245');
});
