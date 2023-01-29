--Procedure
    --INSERT Order
CREATE OR REPLACE PROCEDURE InsertOrder(
    IN UserId INTEGER,
    IN OrderTotalPrice FLOAT
)
LANGUAGE plpgsql
AS $$
    BEGIN
        INSERT INTO Orders(OrderId,UserId,OrderTotalPrice)
        VALUES(nextval('OrderId_Sequence'),UserId,OrderTotalPrice);
    END
$$;
--CALL InsertOrder();

    --INSERT Item_Order
CREATE OR REPLACE PROCEDURE InsertItem_Order(
    IN OrderId INTEGER,
    IN ProductId INTEGER,
    IN ProductQuantity INTEGER
)
LANGUAGE plpgsql
AS $$
    BEGIN
        INSERT INTO Item_Order(Item_OrderId,OrderId, ProductId, ProductQuantity)
        VALUES(nextval('Item_OrderId_Sequence'),OrderId, ProductId, ProductQuantity);
    END
$$;
--CALL InsertItem_Order();

    --INSERT Invoice
CREATE OR REPLACE PROCEDURE InsertInvoice(
    IN UserId INTEGER,
    IN InvoiceDate timestamp,
    IN InvoiceTotalPrice FLOAT,
    IN InvoiceOrderId INTEGER,
    IN InvoiceAddress VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
    BEGIN
        INSERT INTO Invoice(InvoiceId,UserId, InvoiceDate, InvoiceTotalPrice, InvoiceOrderId, InvoiceAddress)
        VALUES(nextval('InvoiceId_Sequence'),UserId, InvoiceDate, InvoiceTotalPrice, InvoiceOrderId, InvoiceAddress);
    END
$$;
--CALL InsertInvoice();

    --INSERT Acquisition
CREATE OR REPLACE PROCEDURE InsertAcquisition(
    IN UserId INTEGER,
    IN AcquisitionDate timestamp
)
LANGUAGE plpgsql
AS $$
    BEGIN
        INSERT INTO Acquisition(AcquisitionId,UserId, AcquisitionDate)
        VALUES(nextval('AcquisitionId_Sequence'),UserId, AcquisitionDate);
    END
$$;
--CALL InsertAcquisition();