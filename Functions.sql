--Functions
    --Total de encomendas feitas até a uma dada data
CREATE OR REPLACE FUNCTION total_encomendas(IN data date)
RETURNS TABLE (OrderId INTEGER,UserId INTEGER,order_data timestamp,OrderStatus VARCHAR(100),OrderTotalPrice FLOAT)
LANGUAGE plpgsql
AS $$
    BEGIN
        RETURN QUERY
            SELECT * FROM orders WHERE orderdate <= data;
    END
$$;
--SELECT * FROM total_encomendas('2023-01-15');

    --Total de encomendas feitas entre duas datas
CREATE OR REPLACE FUNCTION total_encomendas_entre_datas(IN data1 date)
RETURNS TABLE (OrderId INTEGER,UserId INTEGER,order_data timestamp,OrderStatus VARCHAR(100),OrderTotalPrice FLOAT)
LANGUAGE plpgsql
AS $$
    BEGIN
        RETURN QUERY
            SELECT * FROM orders WHERE orderdate BETWEEN AND ;
    END
$$;

CREATE OR REPLACE FUNCTION total_encomendas_entre_datas(IN data1 varchar)
RETURNS TABLE (OrderId INTEGER,UserId INTEGER,order_data timestamp,OrderStatus VARCHAR(100),OrderTotalPrice FLOAT)
LANGUAGE plpgsql
AS $$
DECLARE
    date1 date;
    date2 date;
BEGIN
    date1 := to_date(substring(data1, 1, 10), 'YYYY-MM-DD');
    date2 := to_date(substring(data1, 12), 'YYYY-MM-DD');
    RETURN QUERY
        SELECT * FROM orders WHERE orderdate BETWEEN date1 AND date2;
END
$$;

SELECT * FROM total_encomendas_entre_datas('2023-01-14.2023-01-15');

    --Top Selling Products
CREATE OR REPLACE FUNCTION top_selling_products()
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
    BEGIN
        RETURN (
            SELECT productid
            FROM item_order
            JOIN orders ON item_order.orderid = orders.orderid
            GROUP BY productid
            ORDER BY COUNT(productid) DESC
        LIMIT 1);
END;
$$;
SELECT * from top_selling_products();

    --Top 5 most expensive orders
CREATE OR REPLACE FUNCTION get_top_expensive_orders()
RETURNS TABLE (order_id INTEGER, user_id INTEGER, total_price DOUBLE PRECISION)
LANGUAGE plpgsql
AS $$
    BEGIN
        RETURN QUERY
        SELECT orderid, userid,MAX(ordertotalprice) as total_price
        FROM orders
        GROUP BY orderid
        ORDER BY total_price DESC
        LIMIT 5;
    END;
$$;
SELECT * from get_top_expensive_orders();
