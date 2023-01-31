CREATE TABLE IF NOT EXISTS Orders(
    OrderId INTEGER PRIMARY KEY,
    UserId INTEGER NOT NULL,
    OrderDate timestamp DEFAULT CURRENT_TIMESTAMP,
    OrderStatus VARCHAR(100) DEFAULT 'Em espera',
    OrderTotalPrice FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS Item_Order(
    Item_OrderId INTEGER PRIMARY KEY,
    OrderId INTEGER NOT NULL,
    ProductId INTEGER NOT NULL,
    ProductQuantity INTEGER NOT NULL,
    ProductPrice FLOAT NOT NULL,
    CONSTRAINT fk_Orders
      FOREIGN KEY(OrderId)
	  REFERENCES Orders(OrderId)
);
