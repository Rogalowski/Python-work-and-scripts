
function sendNotification() 
{
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
  
  

  
  var subject = '*WAŻNE* Zakupy na Krzywka80_Wydatki!!! '+ filtrval+' '+sheet.getName();
  var recipientbuyer = '';
  var recipientcleaner = '';
var month = date.getMonth();

  var body = 
 

       '<html><head> '
        
  +'<h3>Sieeemanko załogo na Krzywka :) <br> Cześć ' +personbuyer+ ' i '+personcleaner+' ;) </h3>'

+'<p><b> Właśnie skończył się termin ważności filtra  do dzbanka, który upłynął <span style="color:green;font-size: 18px;">'+date.getDate()+' dnia '+(month+1)+' miesiąca ' +date.getFullYear()+' roku</span>. <span style="color:blue;font-size: 24px;"> <br>'+ personbuyer + '</span>, aktualnie jest <span style="color:red;"> Twoja kolej zakupów</span>, więc proszę kup/zamów/wymień filtr do wody, albo dogadaj się z kimś jeszcze.<br>'
+ ' <span style="color:red;">Natomiast kolej sprzątania ma teraz: </span> <span style="color:blue;font-size: 24px;">'+ personcleaner + '</span>, proszę dogadajcie się razem ;) <br>'
+ 'Zamówić można do odbioru w Galaxy np.: z tej strony: <a href="https://www.mediaexpert.pl/wklady-filtrujace/wklad-filtrujacy-aquaphor-a5-mg,id-1366596">Zamawiamy AQUAPHOR A5 MG pod tym właśnie linkiem</a> <br>' 
+ 'Zamówienie nie wymaga rejestrowania się, więc na spokojnie można zamówić na kogo kolwiek z płatnością przy odbiorze.<br>Jeśli masz problem, daj proszę znać.</p></b>'

+'<h3>Link do pliku Na Krzywka: <a href="https://docs.google.com/spreadsheets/d/1-_FSWuMEnecoWyjdI3NiPNvbSnwrodbFHfEhL2WMs7c/edit#gid=0  ">Zakupy na Krzywka80_Wydatki_Sprzątanko!!!</a> </h3>'
+'<img src="https://www.mediaexpert.pl/media/cache/gallery/product/2/676/444/549/68ajtn5m/images/18/1872015/A5_MG_2__1.jpg" alt="Girl in a jacket" width="500" height="300">'
+'<h3>Pozdrawiam</h3>'

+'<h3>Krzywkowy BOT</h3>'


+'*Wiadomość przesłana automatycznie, proszę nie odpowiadaj na nią*'
 
      '</head>'
  +
  '<body>'
  '</body></html>'
  
  ;
  if((filtrval=='WYMIENIĆ/KUPIĆ FILTR!!! :(') && ((personcleaner!='Ja') || (personbuyer!='Ja'))){
      
      if(personbuyer=="Jacek")
      {
      recipientbuyer = "rogalowski@gmail.com";
      } else
         if(personbuyer=="Magda")
      {
      recipientbuyer = "magdalenachabiera@gmail.com";
      } else
         if(personbuyer=="Rafał")
      {
      recipientbuyer = "olekbeatz@gmail.com";
      } else
         if(personbuyer=="Elena")
      {
      recipientbuyer = "kucherukhelena@gmail.com";
      } else
         if(personbuyer=="Jakub")
      {
      recipientbuyer = "jakubwojewoda111@gmail.com";
      } 
    

        
        if (personcleaner=="Jacek")
      {
      recipientcleaner = "rogalowski@gmail.com";
      } else
         if(personcleaner=="Magda")
      {
      recipientcleaner = "magdalenachabiera@gmail.com";
      } else
         if(personcleaner=="Rafał")
      {
      recipientcleaner = "olekbeatz@gmail.com";
      } else
         if(personcleaner=="Elena")
      {
      recipientcleaner = "kucherukhelena@gmail.com";
      } else
         if(personcleaner=="Jakub")
      {
      recipientcleaner = "jakubwojewoda111@gmail.com";
      } 

 // if(cell.indexOf('V3')!=-1) {

   //  if(filtrval=='WYMIENIĆ/KUPIĆ FILTR!!! :('){ 
  MailApp.sendEmail('rogalowski@interia.pl,'+recipientbuyer+','+recipientcleaner, subject, body, {htmlBody: body});
   

  }
//}
  
  
  
 
  

    
 
  
};
