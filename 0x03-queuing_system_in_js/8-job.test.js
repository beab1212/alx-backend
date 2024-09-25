import { expect } from 'chai';
import sinon from 'sinon';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    sinon.spy(console, 'log');
  });

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    sinon.restore();
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('array', queue)).to.throw();
  });

  it('create two new jobs to the queue', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(console.log.calledOnceWith(`Notification job created: ${queue.testMode.jobs[0].id}`)).to.be.true;
  });
});
