function onOpen() {
  SpreadsheetApp.getUi() // Or DocumentApp or SlidesApp or FormApp.
      .createMenu('Custom Menu')
      .addItem('Show alert', 'showAlert')
      .addToUi();
}

function showAlert() {
 
    var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();

  var cell = ss.getActiveCell().getA1Notation();
  var row = ss.getActiveRange().getRow();
  var cellvalue = ss.getActiveCell().getValue().toString();
  var filtrval = SpreadsheetApp.getActiveSheet().getRange('G3').getValue();
  var personbuyer = SpreadsheetApp.getActiveSheet().getRange('V3').getValue();
  var personcleaner = SpreadsheetApp.getActiveSheet().getRange('K4').getValue();
  var date = SpreadsheetApp.getActiveSheet().getRange('J2').getValue();
  var today = SpreadsheetApp.getActiveSheet().getRange('C2').getValue();
  
  
  
  
  
  var ui = SpreadsheetApp.getUi(); // Same variations.
var month = date.getMonth();
  
  
  
   if((filtrval=='WYMIENIĆ/KUPIĆ FILTR!!! :(') && ((personcleaner!='Ja') || (personbuyer!='Ja'))){
  
////////////////////////////////////////////////HTML/////////////////////////////////////////////////     
    var htmlOutput = HtmlService
    .createHtmlOutput(''
                           +  '<html><head> '
        
  +'<h3>Sieeemanko załogo na Krzywka :) <br></h3>'

+'<p><b> Właśnie skończył się termin ważności filtra  do dzbanka, który upłynął <span style="color:green;font-size: 18px;">'+date.getDate()+' dnia '+(month+1)+' miesiąca ' +date.getFullYear()+' roku</span>. <span style="color:blue;font-size: 24px;"> <br>'+ personbuyer + '</span>, aktualnie jest <span style="color:red;"> Twoja kolej zakupów</span>, więc proszę kup/zamów/wymień filtr do wody, albo dogadaj się z kimś jeszcze.<br>'
+ ' <span style="color:red;">Natomiast kolej sprzątania ma teraz: </span> <span style="color:blue;font-size: 24px;">'+ personcleaner + '</span>, proszę dogadajcie się razem ;) <br>'
+ '<br>Zamówić można do odbioru w Galaxy np.: z tej strony: <a href="https://www.mediaexpert.pl/wklady-filtrujace/wklad-filtrujacy-aquaphor-a5-mg,id-1366596">Zamawiamy AQUAPHOR A5 MG pod tym właśnie linkiem</a> <br>' 
+ '<br>Zamówienie nie wymaga rejestrowania się, więc na spokojnie można zamówić na kogo kolwiek z płatnością przy odbiorze.<br>Jeśli masz problem, daj proszę znać.</p></b>'


+'<img src="https://www.mediaexpert.pl/media/cache/gallery/product/2/676/444/549/68ajtn5m/images/18/1872015/A5_MG_2__1.jpg" alt="Girl in a jacket" width="500" height="300">'
+'<h3>Pozdrawiam</h3>'

+'<h3>Krzywkowy BOT</h3>'


    +  '</head>'
 + '<body>'
+  '</body></html>'
                      +'')
   .setWidth(500)
  .setHeight(600);
    //SpreadsheetApp.getUi().showModalDialog(htmlOutput, 'My add-on');
////////////////////////////////////////////////HTML/////////////////////////////////////////////////
     
     
     SpreadsheetApp.getUi().showModalDialog(htmlOutput, '*WAŻNE* Wymina filtru do dzbanka');

  
}
  
}



/////////////////////////////////////////////POPUP////////////////////////////////////////
/////////wkleić po sprawdzeniu warunku////////////////////////
  //var result = ui.alert(
     
 //   'Niestety już czas zmienić filtr od wody :( ',

   
  
 //       + personcleaner +', teraz twój czas sprzątania oraz, ' 
   // + personbuyer + ' twoja kolej zakupów.      Zgadzasz się? Proszę dogadajcie się w sprawie kupna/wymiany',
    
    //  ui.ButtonSet.YES_NO);

  // Process the user's response.
 // if (result == ui.Button.NO) {
    // User clicked "Yes".
 //   ui.alert(';( No to kto teraz kupi/zmieni?');
 // } 
////////////////////////////////////////////////
