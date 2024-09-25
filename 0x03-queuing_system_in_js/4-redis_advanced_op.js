import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(hashKey, key, value) {
  client.hset(hashKey, key, value, redis.print);
}

function displaySchoolValue(hashKey) {
  client.hgetall(hashKey, (_, obj) => {
    console.dir(obj);
  });
}

const hashKey = 'HolbertonSchools';
const data = [['Portland', 50], ['Seattle', 80], ['New York', 20], ['Bogota', 20], ['Cali', 40], ['Paris', 2]];

client.on('ready', () => {
  data.map((data) => {
    setNewSchool(hashKey, data[0], data[1], redis.print);
    return null;
  });
  displaySchoolValue('HolbertonSchools');
});
