// Form radio control of the radio buttons!..

const btnSubmit = document.getElementById("submit");
const loadingImage = document.getElementById("loading-img");

btnSubmit.addEventListener("click", (e) => {
  const items = document.querySelectorAll('input[type="radio"]:checked');
  if (items.length != 9) {
    alert(
      `${items.length} Soruyu cevapladiniz, ${
        9 - items.length
      } tane soruyu cevaplamalısınız!`
    );
  } else {
    showLoading();
  }
});

function showLoading() {
  loadingImage.style.display = "block";
  setTimeout(() => {
    loadingImage.style.display = "none";
  }, 2000);
}

/* 

/* Control of radio button */

/* 
1. Soruda 0-30000$ seçilir ise ikinci sorunun 4. seçeneği aktif olmayacak!
*/

const radio_option_1 = document.getElementById("radio_btn-0");
const radio_option_1_2 = document.getElementById("radio_btn-1");
const radio_option_1_3 = document.getElementById("radio_btn-2");

const radio_option_2_4 = document.getElementById("radio_btn_4-3");
const radio_option_2_1 = document.getElementById("radio_btn_4-0");
const radio_option_2_2 = document.getElementById("radio_btn_4-1");
const radio_option_2_3 = document.getElementById("radio_btn_4-2");

radio_option_1.addEventListener("click", () => {
  radio_option_2_4.disabled = true;
  radio_option_2_2.disabled = false;
  radio_option_2_1.disabled = false;
});

radio_option_1_2.addEventListener("click", () => {
  radio_option_2_4.disabled = false;
  radio_option_2_1.disabled = true;
  radio_option_2_2.disabled = false;
});

radio_option_1_3.addEventListener("click", () => {
  radio_option_2_2.disabled = true;
  radio_option_2_1.disabled = true;
  radio_option_2_4.disabled = false;
});

/* 
5. Soruda 2.1 seçildiyse 5. 3-4-5 secenekleri aktif olmayacak
*/

const option_5_3 = document.getElementById("radio_btn_5-2");
const option_5_4 = document.getElementById("radio_btn_5-3");
const option_5_5 = document.getElementById("radio_btn_5-4");

radio_option_2_1.addEventListener("click", () => {
  option_5_3.disabled = true;
  option_5_4.disabled = true;
  option_5_5.disabled = true;
});

radio_option_2_2.addEventListener("click", () => {
  option_5_3.disabled = false;
  option_5_4.disabled = false;
  option_5_5.disabled = false;
});

radio_option_2_3.addEventListener("click", () => {
  option_5_3.disabled = false;
  option_5_4.disabled = false;
  option_5_5.disabled = false;
});

radio_option_2_4.addEventListener("click", () => {
  option_5_3.disabled = false;
  option_5_4.disabled = false;
  option_5_5.disabled = false;
});

/* 
 6. soru, 2.1 secildiyse 6. 1 seceneği aktif gerisi sönük.
 6. soru, 2.2 secildiyse 6. 2,5,8. seceneği aktif, gerisi sönük.
 6. soru, 2.3 secildiyse 6. 3,6,9. secenek aktif gerisi sönül
 6. soru, 2.4 secildiyse 6. 4,7,10 secenek aktif gerisi sönük
*/

const options_7 = document.getElementsByName("radio_btn_7");

radio_option_2_1.addEventListener("click", () => {
  options_7[0].disabled = false;
  options_7[1].disabled = true;
  options_7[2].disabled = true;
  options_7[3].disabled = true;
  options_7[4].disabled = true;
  options_7[5].disabled = true;
  options_7[6].disabled = true;
  options_7[7].disabled = true;
  options_7[8].disabled = true;
  options_7[9].disabled = true;
});

radio_option_2_2.addEventListener("click", () => {
  options_7[0].disabled = true;
  options_7[1].disabled = false;
  options_7[2].disabled = true;
  options_7[3].disabled = true;
  options_7[4].disabled = false;
  options_7[5].disabled = true;
  options_7[6].disabled = true;
  options_7[7].disabled = false;
  options_7[8].disabled = true;
  options_7[9].disabled = true;
});

radio_option_2_3.addEventListener("click", () => {
  options_7[0].disabled = true;
  options_7[1].disabled = true;
  options_7[2].disabled = false;
  options_7[3].disabled = true;
  options_7[4].disabled = true;
  options_7[5].disabled = false;
  options_7[6].disabled = true;
  options_7[7].disabled = true;
  options_7[8].disabled = false;
  options_7[9].disabled = true;
});

radio_option_2_4.addEventListener("click", () => {
  options_7[0].disabled = true;
  options_7[1].disabled = true;
  options_7[2].disabled = true;
  options_7[3].disabled = false;
  options_7[4].disabled = true;
  options_7[5].disabled = true;
  options_7[6].disabled = false;
  options_7[7].disabled = true;
  options_7[8].disabled = true;
  options_7[9].disabled = false;
});
