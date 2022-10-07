/*
* Account Javascript - Diwido
*/

/**
 *  intl-tel-input-17.0.19 JS
 * https://github.com/jackocnr/intl-tel-input
 */
var input = document.querySelector("#phone");
window.intlTelInput(input, {
  // any initialisation options go here
  autoHideDialCode: false,
  initialCountry: "fr",
  preferredCountries: ['fr', 'us'],
});

/**
 *  country-select-js JS v2.1.1
 * https://github.com/mrmarkfrench/country-select-js/
 */
 $("#country_selector").countrySelect({
  defaultCountry: "fr",
  defaultStyling: "inside",
  preferredCountries: ['fr', 'us'],
  // localized country names e.g. { 'de': 'Deutschland' }
  localizedCountries: null,
  //excludeCountries: ['ch', 'do'],
  //onlyCountries: ['us', 'gb', 'ca']
  responsiveDropdown: true
});
const myData = $("#country_selector").countrySelect("getSelectedCountryData");
//const myData = $.fn.countrySelect.getCountryData();

/**
 * isUrlValid
 * @param {*} url the url to validate
 * @returns the result of the validation as boolean
 */
function isUrlValid(url) {
  const res = url.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
  return res.test(String(url).toLowerCase());
}

/**
 *  Email Validation
 *  https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email#basic_validation
 */
function isEmailValid(email) {
  const res = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return res.test(String(email).toLowerCase());
}

/**
 * Function to validate password
 */ 
const validatePassword = (inputPassword) => inputPassword.value.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);


function isPhoneValid(phone) {
  const res = /^\+[1-9]{1}[0-9]{3,14}$/;
  return res.test(String(phone).toLowerCase());
}


/**
 * isTextValid valies the text input
 * @param {*} form_name form name
 * @param {*} input_name input name
 * @returns the result of the validation as boolean
 */
function isTextInputValid(form_name, input_name) {
  let regName = /\d+$/g;
  let data = document.forms[form_name][input_name].value;
  if (data == "" || regName.test(data)) {
    return false;
  }
  return true;
}

/**
 * nameValidation validates a name input
 * @param {*} input_id the id of the input HTML element
 * @param {*} message_id the id the message HTML element
 * @param {*} is_alphanum is the input alpha numeric
 * @returns the boolean status of the validation 
 */
function nameValidation(input_id, message_id, is_onlyalpha){
  //var input_id = "firstname"
  //var message_id = "firstnameHelp"
  var id = (id) => document.getElementById(id);
  var state = false;

  var fn=id(input_id).value;  
  if(fn == ""){
    message_txt = 'Your profile needs a name';
    state = false;
  }
  //if((/\d+/.test(fn))&&(!is_alphanum)){
  if((is_onlyalpha)&&(/\d+/.test(fn))){  
    message_txt = 'Your name contains numbers';
    state = false;
  }  
  if(fn.length<=6){
    message_txt = 'Your name is to short';
    state = false;
  }
  if(state == false){
    //id(message_id).value=message_txt;
    //id(message_id).innerHTML=message_txt;
    id(message_id).innerText=message_txt;

    alert("state: "+ id(message_id).value);
  
    id(message_id).style.visibility = "visible";
    //id(input_id).insertAdjacentHTML('afterend', '<small id="testHelp" class="form-text alert-text '+
    //  'text-muted" style="visible">TEST TEST</small>');
    return false;
  }
  //default
  id(message_id).style.visibility = "display:none;";
  return true;
}

/**
 * persoinfoValidation validates the Personal Information Form
 */
function profilValidation(){
  //First Name
  nameValidation("firstname", "firstnameHelp", true);
  //Last Name
  nameValidation("lastname", "lastnameHelp", true);
  //About
  //Phone number  
  //Website
  //Username
  nameValidation("username", "usernameHelp", false);
  return true;
}

//triggers when user submits the form

form.addEventListener("submit",(e) => {
  e.preventDefault();
  profilValidation();
});
// Focusout event listener. Triggers when the user clicks anywhere else besides the input
/*
email.addEventListener("focusout", (e)=>{
  nameValidation("firstname", "firstnameHelp", true);
});
*/

/*
jQuery("form").submit(function(e){
  e.de.preventDefault();  
  //or
  //return false;
});
*/

//let id = (id) => document.getElementById(id);
//let classes = (classes) => document.getElementsByClassName(classes);
/*
$(document).ready(function() { 
  $("input").focusout(function() { 
        // If it is not blank.
        $(this).css('border', 'solid 2px green');    
  }) .trigger("focusout");
}); 
*/