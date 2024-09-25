import { promisify } from 'util';
import { createClient } from 'redis';
import express from 'express';

const client = createClient();

client.on('err', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const listProducts = [
  {
    Id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    Id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    Id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    Id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

function changeFormat(product) {
  const newFormate = {};
  newFormate.itemId = product.Id;
  newFormate.itemName = product.name;
  newFormate.price = product.price;
  newFormate.initialAvailableQuantity = product.stock;
  return newFormate;
}

function getItemById(id) {
  for (const product of listProducts) {
    if (product.Id === id) {
      return changeFormat(product);
    }
  }
  return {};
}

function reserveStockById(itemId, stock) {
  const SET = promisify(client.SET).bind(client);
  return SET(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const GET = promisify(client.GET).bind(client);
  const stock = await GET(`item.${itemId}`);
  if (stock === null) return 0;
  return stock;
}

const app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts.map(changeFormat));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length > 0) {
    const stock = await getCurrentReservedStockById(itemId);
    item.currentQuantity = item.initialAvailableQuantity - stock;
    return res.json(item);
  }
  return res.json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (Object.values(item).length === 0) {
    return res.json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  if (stock >= item.initialAvailableQuantity) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, Number(stock) + 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

function clearRedisStock() {
  const SET = promisify(client.SET).bind(client);
  return Promise.all(listProducts.map((item) => SET(`item.${item.Id}`, 0)));
}

app.listen(1245, async () => {
  await clearRedisStock();
});
