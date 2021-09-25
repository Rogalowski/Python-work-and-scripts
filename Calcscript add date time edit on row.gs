function onEdit(event)
{ 
  var timezone = "GMT+2";
  var timestamp_format = "dd MM-YYYY HH:mm"; // Timestamp Format. 
  //var updateColName = "SUMA WYDATKÓW Z CAŁEGO ROKU:";
  
  var updateColName = ["raz", "dwa", "trzy", "cztery", "piec"]; 
  var timeStampColName = "dwa";
  //var timeStampColName = "Dziś jest:";
  
  //SpreadsheetApp.getActiveSpreadsheet()
  var sheet = event.source.getSheetByName('2021');
  
  
  //var sheet = event.source.getActiveSheet(); //Name of the sheet where you want to run this script.
  //var sheet = event.source.getActiveSheet();

  
   for (var i = 0; i < updateColName.length; i++) {
  
  var actRng = event.source.getActiveRange();
  var editColumn = actRng.getColumn();
  var index = actRng.getRowIndex();
  var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues();
  var dateCol = headers[0].indexOf(timeStampColName);
  var updateCol = headers[0].indexOf(updateColName[i]); updateCol = updateCol+1;
  if (dateCol > -1 && index > 1 && editColumn == updateCol) { // only timestamp if 'Last Updated' header exists, but not in the header row itself!
    var cell = sheet.getRange(index , dateCol + 1);
    var date = Utilities.formatDate(new Date(), timezone, timestamp_format);
    cell.setValue(date);
   }
  }
}

