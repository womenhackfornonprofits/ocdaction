const navigation = document.getElementsByClassName('js-header-nav')[0];
const menuEl = document.getElementsByClassName('js-header-list')[0]

navigation.addEventListener('click', function (event) {
    const srcElementClass = event.target.className;
	if (srcElementClass.match('js-nav-toggle')) {
		menuEl.classList.toggle('header__list--mobile')
	} else {
		menuEl.classList.remove('header__list--mobile')
	}
});

var birthYear = document.getElementById('id_date_birth_year');
var birthMonth = document.getElementById('id_date_birth_month');
var birthDay = document.getElementById('id_date_birth_day');

// Javascript uses a Month Index of 0-11
var birthMonthIndex = Number(birthMonth.value) - 1;

birthYear.onchange = function () {
  var birthday = new Date(birthYear.value, birthMonthIndex, birthDay.value);
  var age = calculateAge(birthday)
  checkYoungerThanEighteen(age)
}

birthMonth.onchange = function () {
  birthMonthIndex = Number(birthMonth.value) - 1;
  var birthday = new Date(birthYear.value, birthMonthIndex, birthDay.value);
  var age = calculateAge(birthday)
  checkYoungerThanEighteen(age)
} 

birthDay.onchange = function () {
  var birthday = new Date(birthYear.value, birthMonthIndex, birthDay.value);
  var age = calculateAge(birthday)
  checkYoungerThanEighteen(age)
}

function calculateAge(dateString) {
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}

// Function checks if user is younger than Eighteen, if true disable Register button
function checkYoungerThanEighteen(age)
{
  if (age < 18) 
  {
    var x = document.getElementsByClassName("button col-xs-4")[0];
    x.disabled=true;
    alert('You have to be 18 or over to continue');
  } 
  else
  {
    var x = document.getElementsByClassName("button col-xs-4")[0];
    x.disabled=false;
  }  
}