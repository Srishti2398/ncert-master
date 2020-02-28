var stateObject = {
"India": 
{ 
"Maharashtra": ["Akola", "Amravati", "Buldhana", "Washim", "Yavatmal",'Aurangabad','Beed','Jalna','Osmanabad','Nanded','Latur','Parbhani','Hingoli'],
"Kerala": ["Thiruvananthapuram", "Palakkad"],
"Goa": ["North Goa", "South Goa"],
},

}


var learningObject = {
"8": 
{ 
"Science": ["Classifies materials and organisms based on properties/characteristics", "Conducts simple investigation to seek answers to queries", "Relates processes and phenomenon with causes", "measures and calculates e.g., temperature; pulse rate; speed of moving objects; time period of a simple pendulum, etc", "plots and interprets graphs",'Constructs models using materials from surroundings and explains their working','Differentiates materials, organism and processes','Relates processes and phenomenon with causes','Explains processes and phenomenon','measures angles of incidence and reflection, etc.','Applies learning of scientific concepts in day-to-day life','Makes efforts to protect environment'],
"Social Science": ["ss1", "ss2"],
"Math": ["m1", "m2"],
"Language": ["l1", "l2"],
},

}
function blinker() {
    $('.blink').fadeOut(500).fadeIn(500);
}
 
setInterval(blinker, 1000);




window.onload = function () {

        var countySel = document.getElementById("countySel"),
        stateSel = document.getElementById("stateSel"),
        districtSel = document.getElementById("districtSel");
        for (var country in stateObject) {
          countySel.options[countySel.options.length] = new Option(country, country);
        }
        countySel.onchange = function () {
          stateSel.length = 1; // remove all options bar first
          districtSel.length = 1; // remove all options bar first
          if (this.selectedIndex < 1) return; // done 
          for (var state in stateObject[this.value]) {
            stateSel.options[stateSel.options.length] = new Option(state, state);
          }
        }
        countySel.onchange(); // reset in case page is reloaded
        stateSel.onchange = function () {
          districtSel.length = 1; // remove all options bar first
          if (this.selectedIndex < 1) return; // done 
          var district = stateObject[countySel.value][this.value];
          for (var i = 0; i < district.length; i++) {
            districtSel.options[districtSel.options.length] = new Option(district[i], district[i]);
          }
        }

        var classSel = document.getElementById("classSel"),
        subjectSel = document.getElementById("subjectSel"),
        learningSel = document.getElementById("learningSel");
        for (var classs in learningObject) {
        classSel.options[classSel.options.length] = new Option(classs, classs);
        }
        classSel.onchange = function () {
        subjectSel.length = 1; // remove all options bar first
        learningSel.length = 1; // remove all options bar first
        if (this.selectedIndex < 1) return; // done 
        for (var subject in learningObject[this.value]) {
        subjectSel.options[subjectSel.options.length] = new Option(subject, subject);
        }
        }
        classSel.onchange(); // reset in case page is reloaded
        subjectSel.onchange = function () {
        learningSel.length = 1; // remove all options bar first
        if (this.selectedIndex < 1) return; // done 
        var learning = learningObject[classSel.value][this.value];
        for (var i = 0; i < learning.length; i++) {
        learningSel.options[learningSel.options.length] = new Option(learning[i], learning[i]);
        }
        }



        


}