const multiStepForm = document?.querySelector("[data-multi-step]");
const formSteps = [...multiStepForm?.querySelectorAll("[data-step]")];
const buttons = document?.querySelectorAll("button");

let currentStep = formSteps?.findIndex((step) => {
  return step.classList.contains("active");
});

// Otomatik olarak birinci formu gösteriri
if (currentStep < 0) {
  currentStep = 0;
  showCurrentStep();
}

multiStepForm.addEventListener("click", (e) => {
  const radios = document.getElementsByName("radio_btn");
  const radios_2 = document.getElementsByName("radio_btn_2");
  const radios_5 = document.getElementsByName("radio_btn_5");
  const radios_6 = document.getElementsByName("radio_btn_6");

  console.log("Soru " + currentStep);

  /* 1. sorunun 1. seçeneği seçili ise 2. sorunun 4. seceneği aktif olmayacak!
     1. sorunun 2. seceneği secili ise 2. sorunun 1. seceneği aktif olmayacak!
     1. sorunun 3. seceneği secili ise 2. sorunun 1-2 secenekleri aktif olmayacak!
  */
  if (radios[0].checked) {
    radios_2[0].disabled = false;
    radios_2[1].disabled = false;
    radios_2[2].disabled = false;
    radios_2[3].disabled = true;
  } else if (radios[1].checked) {
    radios_2[0].disabled = true;
    radios_2[1].disabled = false;
    radios_2[2].disabled = false;
    radios_2[3].disabled = false;
  } else if (radios[2].checked) {
    radios_2[0].disabled = true;
    radios_2[1].disabled = true;
    radios_2[2].disabled = false;
    radios_2[3].disabled = false;
  }

  // 2. sorunun 1. seceneği secili ise 5. sorunun 3-4-5 secenekleri aktif olmayacak
  // 2. sorunun 2. seceneği secilirse 5. sorunun 5. seceneği aktif olmayacak
  if (currentStep === 3) {
    if (radios_2[0].checked) {
      radios_5[2].disabled = true;
      radios_5[3].disabled = true;
      radios_5[4].disabled = true;
    } else if (radios_2[1].checked) {
      radios_5[4].disabled = true;
    } else {
      radios_5[2].disabled = false;
      radios_5[3].disabled = false;
      radios_5[4].disabled = false;
      radios_5[4].disabled = false;
    }
  }
  /*
     2.1 secildiyse 6. 1 seceneği aktif gerisi sönük.
     2.2 secildiyse 6. 2,5,8. seceneği aktif, gerisi sönük.
     2.3 secildiyse 6. 3,6,9. secenek aktif gerisi sönül
     2.4 secildiyse 6. 4,7,10 secenek aktif gerisi sönük
    */

  if (currentStep === 4) {
    if (radios_2[0].checked) {
      radios_6[0].disabled = false;
      radios_6[1].disabled = true;
      radios_6[2].disabled = true;
      radios_6[3].disabled = true;
      radios_6[4].disabled = true;
      radios_6[5].disabled = true;
      radios_6[6].disabled = true;
      radios_6[7].disabled = true;
      radios_6[8].disabled = true;
      radios_6[9].disabled = true;
    } else if (radios_2[1].checked) {
      radios_6[0].disabled = true;
      radios_6[1].disabled = false;
      radios_6[2].disabled = true;
      radios_6[3].disabled = true;
      radios_6[4].disabled = false;
      radios_6[5].disabled = true;
      radios_6[6].disabled = true;
      radios_6[7].disabled = true;
      radios_6[8].disabled = false;
      radios_6[9].disabled = true;
    } else if (radios_2[2].checked) {
      radios_6[0].disabled = true;
      radios_6[1].disabled = true;
      radios_6[2].disabled = false;
      radios_6[3].disabled = true;
      radios_6[4].disabled = true;
      radios_6[5].disabled = false;
      radios_6[6].disabled = true;
      radios_6[7].disabled = true;
      radios_6[8].disabled = false;
      radios_6[9].disabled = true;
    } else if (radios_2[3].checked) {
      radios_6[0].disabled = true;
      radios_6[1].disabled = true;
      radios_6[2].disabled = true;
      radios_6[3].disabled = false;
      radios_6[4].disabled = true;
      radios_6[5].disabled = true;
      radios_6[6].disabled = false;
      radios_6[7].disabled = true;
      radios_6[8].disabled = true;
      radios_6[9].disabled = false;
    }
  }

  let incrementor;

  if (e.target.matches("[data-next]")) {
    incrementor = 1;
  } else if (e.target.matches("[data-previous]")) {
    incrementor = -1;
  } else {
    return;
  }
  const inputs = [...formSteps[currentStep].querySelectorAll("input")];
  const allValid = inputs.every((input) => input.checkValidity());
  if (allValid) {
    currentStep += incrementor;
  }
  showCurrentStep();
});

function showCurrentStep() {
  formSteps.forEach((step, index) => {
    step.classList.toggle("active", index === currentStep);
  });
}

// Form radio control of the radio buttons!..

const btnSubmit = document.getElementById("submit");
const loadingImage = document.getElementById("loading-img");

btnSubmit.addEventListener("click", (e) => {
  const items = document.querySelectorAll('input[type="radio"]:checked');
  if (items.length != 8) {
    alert(
      `${items.length} Soruyu cevapladiniz, ${
        8 - items.length
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
