const express = require("express");

const { KintoneRestAPIClient } = require("@kintone/rest-api-client");
const config = require("./config.json");

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const client = new KintoneRestAPIClient({
  baseUrl: "https://zehao-qian.kintone.com",
  auth: { apiToken: config.apiToken },
});

app.get("/nodebridge/get-records", function (req, res) {
  client.record
    .getRecords({ app: config.AppID })
    .then((kintoneResponse) => {
      res.json(kintoneResponse.records);
    })
    .catch((err) => {
      console.error(err);
      res.status(500).send("Error fetching records from Kintone");
    });
});

app.post("/nodebridge/add-record", (req, res) => {
  const recordData = req.body;
  console.log(req.body);
  client.record
    .addRecord({
      app: config.AppID,
      record: recordData,
    })
    .then((resp) => {
      res.status(200).send({ message: "Record added", id: resp.id });
    })
    .catch((error) => {
      console.error("Error adding record:", error);
      res.status(500).send({ message: "Error adding record", error });
    });
});

// const port = 3000;
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
