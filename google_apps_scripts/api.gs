const sheet = SpreadsheetApp.getActive().getSheetByName("Sheet1");

function doPost(e) {
  let data = { status: 0 };
  if (e.parameter.action) {
    const action = e.parameter.action.toLowerCase();
    switch (action) {
      case "update":
        if (update(sheet, JSON.parse(e.postData.getDataAsString()))) {
          data["status"] = 1;
        } else {
          data["status"] = -1;
        }
        break;
    }
  }
  const payload = JSON.stringify(data);
  const response = ContentService.createTextOutput();
  response.setMimeType(ContentService.MimeType.JSON);
  response.setContent(payload);
  return response;
}

function update(sheet, postData) {
  let row = createRow(sheet, postData);
  if (row) {
    sheet.appendRow(row);
    return true;
  } else {
    return false;
  }
}

function createRow(sheet, postData) {
  postData["Date"] = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy/MM/dd HH:mm");
  const keys = sheet.getDataRange().getValues()[0];
  let row = [];
  for (const key of keys) {
    const value = postData[key];
    if (value) {
      row.push(value);
    } else {
      return false;
    }
  }
  return row;
}
