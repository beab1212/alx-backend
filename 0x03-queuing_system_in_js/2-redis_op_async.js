import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const get = promisify(client.get).bind(client);
  get(schoolName).then((data) => {
    console.log(data);
  }).catch((err) => {
    console.log(err);
  });
}

client.on('ready', async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
});
