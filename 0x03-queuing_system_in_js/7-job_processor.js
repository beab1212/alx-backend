import { createQueue } from 'kue';

const queue = createQueue();

const blackListedPhones = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  if (blackListedPhones.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  const totalFrames = 100;
  function next(frame) {
    if (frame === 0 || frame === (totalFrames / 2)) {
      job.progress(frame, totalFrames);
      if (frame === (totalFrames / 2)) {
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      }
    }
    if (frame === totalFrames) {
      return done();
    }
    return next(frame + 1);
  }
  next(0);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
