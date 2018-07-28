var myjson = 'pollutionbystateandyearv2.json'
var year = [];
var nomean = [];
var omean = [];
var somean = [];
var comean = [];

//when button click, run function 
function GetSelectedValues(){
  //variables
  var year = [];
  var years = [];
  var nomean = [];
  var omean = [];
  var somean = [];
  var comean = [];
  var yearnomean = [];
  var yearomean = [];
  var yearsomean = [];
  var yearcomean = [];
  var totalnomean = 0;
  var totalomean = 0;
  var totalsomean = 0;
  var totalcomean = 0;

  //get data from drop down
  var stateSelect = document.getElementById("states-dropdown").value;
  var yearSelect = document.getElementById("year-dropdown").value;
  // var monthSelect = document.getElementById("month-dropdown").value;
  //print values in console
  console.log(stateSelect)
  console.log(yearSelect)
  // console.log(monthSelect)

  //read json
  $.getJSON(myjson, function(data){
    //retreive all indexes where the state abbreivation(stateabbr) is equal to the state selected
    //from state drop-down bar
    data,stateIndices = data.reduce((r,o,i)=> (o.stateabbr === stateSelect && r.push(i), r), []);
    console.log(stateIndices)
    //from year drop-down bar
    data,yearIndices = data.reduce((r, o, i) => ((o.Year === yearSelect && o.stateabbr === stateSelect ) && r.push(i), r), []);
    console.log(yearIndices)

    //Loop, retreive and append pollution data into variable lists
    for (var i = 0; i < stateIndices.length; i++){
      years.push(data[i].Year);
      nomean.push(data[i].AvgNO2);
      omean.push(data[i].AvgO3);
      somean.push(data[i].AvgS2);
      comean.push(data[i].AvgCO);
    };
    //Loop, retreive and append pollution data into variable lists by State abd Month
    for (var i = 0; i < yearIndices.length; i++){
      year.push(data[i].Year);
      yearnomean.push(data[i].AvgNO2);
      yearomean.push(data[i].AvgO3);
      yearsomean.push(data[i].AvgS2);
      yearcomean.push(data[i].AvgCO);
    }
    //Loop, retreive and add all values in their respected lists
    for (var i = 0; i < stateIndices.length; i++){
      totalnomean += nomean[i];
      totalomean += omean[i];
      totalsomean += somean[i];
      totalcomean += comean[i];
    };
    //print values in console
    console.log(totalnomean);
    console.log(totalomean);  
    console.log(totalsomean);
    console.log(totalcomean);
    console.log(nomean)

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'polarArea',
      data:{
        labels: ["Nitrogen Dioxide","Ozone","Sulfur Dioxide","Carbon Dioxide"],
        datasets:[
          {
            label: years[0],
            backgroundColor: ["#F9EBEA", "#EBF5FB", "#F7DC6F", "#D7DBDD"],
            data: [nomean[0], omean[0], somean[0], comean[0]]
          },{
            label: years[1],
            backgroundColor: ["#F2D7D5", "#D6EAF8", "#F7DC6F", "#D7DBDD"],
            data: [nomean[1], omean[1], somean[1], comean[1]]
          },{
            label: years[2],
            backgroundColor: ["#E6B0AA", "#AED6F1", "#F7DC6F", "#D7DBDD"],
            data: [nomean[2], omean[2], somean[2], comean[2]]
          },{
            label: years[3],
            backgroundColor: ["#D98880", "#85C1E9", "#F7DC6F", "#D7DBDD"],
            data: [nomean[3], omean[3], somean[3], comean[3]]
          },{
            label: years[4],
            backgroundColor: ["#CD6155", "#AED6F1", "#F7DC6F", "#D7DBDD"],
            data: [nomean[4], omean[4], somean[4], comean[4]]
          },{
            label: years[5],
            backgroundColor: ["#C0392B", "#5DADE2", "#F7DC6F", "#D7DBDD"],
            data: [nomean[5], omean[5], somean[5], comean[5]]
          },{
            label: years[6],
            backgroundColor: ["#A93226", "#3498DB", "#F7DC6F", "#D7DBDD"],
            data: [nomean[6], omean[6], somean[6], comean[6]]
          },{
            label: years[7],
            backgroundColor: ["#922B21", "#2E86C1", "#F7DC6F", "#D7DBDD"],
            data: [nomean[7], omean[7], somean[7], comean[7]]
          },{
            label: years[8],
            backgroundColor: ["#7B241C", "#2874A6", "#F7DC6F", "#D7DBDD"],
            data: [nomean[8], omean[8], somean[8], comean[8]]
          },{
            label: years[9],
            backgroundColor: ["#641E16", "#1B4F72", "#F7DC6F", "#D7DBDD"],
            data: [nomean[9], omean[9], somean[9], comean[9]]
          },{
            label: years[10],
            backgroundColor: ["#641E16", "#1B4F72", "#F7DC6F", "#D7DBDD"],
            data: [nomean[10], omean[10], somean[10], comean[10]]
          }
        ]
      }
    })
    var ctx = document.getElementById('myChart1').getContext('2d');
    var myChart1 = new Chart(ctx, {
      type: 'bar',
      data:{
        labels:["Nitrogen Dioxide","Ozone","Sulfur Dioxide","Carbon Dioxide"],
        datasets:[
        {
          label: year,
          backgroundColor: ["#F9EBEA", "#EBF5FB", "#F7DC6F", "#D7DBDD"],
          data: [yearnomean, yearomean, yearsomean, yearcomean]
        }]
      }
    })
  })
}

// function GetSelectedValues(){
//     //variables
//   var year = [];
//   var nomean = [];
//   var omean = [];
//   var somean = [];
//   var comean = [];
//   var totalnomean = 0;
//   var totalomean = 0;
//   var totalsomean = 0;
//   var totalcomean = 0;

//   //get data from drop down
//   var stateSelect = document.getElementById("states-dropdown").value;
//   var yearSelect = document.getElementById("year-dropdown").value;
//   // var monthSelect = document.getElementById("month-dropdown").value;
//   //print values in console
//   console.log(stateSelect)
//   console.log(yearSelect)
//   // console.log(monthSelect)

//   //read json
//   $.getJSON(myjson, function(data){
//     //retreive all indexes where the state abbreivation(stateabbr) is equal to the state selected
//     //from state drop-down bar
//     data,stateIndices = data.reduce((r,o,i)=> (o.stateabbr === stateSelect && r.push(i), r), []);
//     console.log(stateIndices)
//     //from year drop-down bar
//     data,yearIndices = data.reduce((r, o, i) => ((o.Year === yearSelect && o.stateabbr === stateSelect ) && r.push(i), r), []);
//     console.log(yearIndices)

//     //Loop, retreive and append pollution data into variable lists
//     for (var i = 0; i < yearIndices.length; i++){
//       year.push(data[i].Year);
//       nomean.push(data[i].AvgNO2);
//       omean.push(data[i].AvgO3);
//       somean.push(data[i].AvgS2);
//       comean.push(data[i].AvgCO);
//     };
//     //print values in console
//     console.log(totalnomean);
//     console.log(totalomean);  
//     console.log(totalsomean);
//     console.log(totalcomean);
//   })
// }




// function GetSelectedValues(){
//     $.getJSON(myjson, function(data){
//     //retreive all indexes where the state abbreivation(stateabbr) is equal to the state selected
//     //from state drop-down bar
//     data,yearIndices = data.reduce((r, o, i) => ((o.Year === yearSelect && o.stateabbr === stateSelect ) && r.push(i), r), []);
//     //test data indexes
//     console.log(yearIndices)




// [
//       {
//         label: [],
//         backgroundColor: [],
//         data: [totalnomean, totalomean, totalsomean, totalcomean]
//       }
//     ]