--Views
    --Order
CREATE OR REPLACE VIEW OrdersView
AS
    SELECT Orders.OrderId, Orders.UserId, Orders.OrderDate, Orders.OrderStatus, Orders.OrderTotalPrice
    FROM Orders;
--SELECT * FROM OrdersView;

    --Invoice
CREATE OR REPLACE VIEW InvoiceView
AS
    SELECT Invoice.InvoiceId, Invoice.UserId, Invoice.InvoiceDate, Invoice.InvoiceTotalPrice, Invoice.InvoiceOrderId, Invoice.InvoiceAddress
    FROM Invoice JOIN Orders
    ON Invoice.InvoiceOrderId = Orders.OrderId;
--SELECT * FROM InvoiceView;

    --Acquisition
CREATE OR REPLACE VIEW AcquisitionView
AS
    SELECT Acquisition.AcquisitionId, Acquisition.AcquisitionDate
    FROM Acquisition;
--SELECT * FROM AcquisitionView;