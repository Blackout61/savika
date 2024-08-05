const multiStepForm = document?.querySelector("[data-multi-step]");
const sorular = [...multiStepForm?.querySelectorAll("[soru]")];
const buttons = document?.querySelectorAll("button");

console.log("sorular", sorular);

let currentStep = 0;

// Otomatik olarak birinci formu gösteriri
if (currentStep === 0) {
  showCurrentStep();
}

multiStepForm.addEventListener("click", (e) => {
  const radios = document.getElementsByName("radio_btn");
  const radios_2 = document.getElementsByName("radio_btn_2");
  const radios_5 = document.getElementsByName("radio_btn_5");
  const radios_6 = document.getElementsByName("radio_btn_6");

  const liElements_2 = document.querySelectorAll("#radio_btn_2 li");
  const liElements_5 = document.querySelectorAll("#radio_btn_5 li");
  const liElements_6 = document.querySelectorAll("#radio_btn_6 li");

  console.log("Soru " + currentStep);

  /* 1. sorunun 1. seçeneği seçili ise 2. sorunun 4. seceneği aktif olmayacak!
     1. sorunun 2. seceneği secili ise 2. sorunun 1. seceneği aktif olmayacak!
     1. sorunun 3. seceneği secili ise 2. sorunun 1-2 secenekleri aktif olmayacak!
  */
  if (radios[0].checked) {
    liElements_2[0].classList.remove("hidden");
    liElements_2[1].classList.remove("hidden");
    liElements_2[2].classList.remove("hidden");
    liElements_2[3].classList.add("hidden");
  } else if (radios[1].checked) {
    liElements_2[0].classList.add("hidden");
    liElements_2[1].classList.remove("hidden");
    liElements_2[2].classList.remove("hidden");
    liElements_2[3].classList.remove("hidden");
  } else if (radios[2].checked) {
    liElements_2[0].classList.add("hidden");
    liElements_2[1].classList.add("hidden");
    liElements_2[2].classList.remove("hidden");
    liElements_2[3].classList.remove("hidden");
  }

  // 2. sorunun 1. seceneği secili ise 5. sorunun 3-4-5 secenekleri aktif olmayacak
  // 2. sorunun 2. seceneği secilirse 5. sorunun 5. seceneği aktif olmayacak
  if (currentStep === 3) {
    if (radios_2[0].checked) {
      liElements_5[2].classList.add("hidden");
      liElements_5[3].classList.add("hidden");
      liElements_5[4].classList.add("hidden");
    } else if (radios_2[1].checked) {
      liElements_5[2].classList.remove("hidden");
      liElements_5[3].classList.remove("hidden");
      liElements_5[4].classList.add("hidden");
    } else {
      radios_5[2].disabled = false;
      radios_5[3].disabled = false;
      radios_5[4].disabled = false;
      radios_5[4].disabled = false; //+++++?????
      liElements_5[2].classList.remove("hidden");
      liElements_5[3].classList.remove("hidden");
      liElements_5[4].classList.remove("hidden");
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
      liElements_6[0].classList.remove("hidden");
      liElements_6[1].classList.add("hidden");
      liElements_6[2].classList.add("hidden");
      liElements_6[3].classList.add("hidden");
      liElements_6[4].classList.add("hidden");
      liElements_6[5].classList.add("hidden");
      liElements_6[6].classList.add("hidden");
      liElements_6[7].classList.add("hidden");
      liElements_6[8].classList.add("hidden");
      liElements_6[9].classList.add("hidden");
    } else if (radios_2[1].checked) {
      liElements_6[0].classList.add("hidden");
      liElements_6[1].classList.remove("hidden");
      liElements_6[2].classList.add("hidden");
      liElements_6[3].classList.add("hidden");
      liElements_6[4].classList.remove("hidden");
      liElements_6[5].classList.add("hidden");
      liElements_6[6].classList.add("hidden");
      liElements_6[7].classList.remove("hidden");
      liElements_6[8].classList.add("hidden");
      liElements_6[9].classList.add("hidden");
    } else if (radios_2[2].checked) {
      liElements_6[0].classList.add("hidden");
      liElements_6[1].classList.add("hidden");
      liElements_6[2].classList.remove("hidden");
      liElements_6[3].classList.add("hidden");
      liElements_6[4].classList.add("hidden");
      liElements_6[5].classList.remove("hidden");
      liElements_6[6].classList.add("hidden");
      liElements_6[7].classList.add("hidden");
      liElements_6[8].classList.remove("hidden");
      liElements_6[9].classList.add("hidden");
    } else if (radios_2[3].checked) {
      liElements_6[0].classList.add("hidden");
      liElements_6[1].classList.add("hidden");
      liElements_6[2].classList.add("hidden");
      liElements_6[3].classList.remove("hidden");
      liElements_6[4].classList.add("hidden");
      liElements_6[5].classList.add("hidden");
      liElements_6[6].classList.remove("hidden");
      liElements_6[7].classList.add("hidden");
      liElements_6[8].classList.add("hidden");
      liElements_6[9].classList.remove("hidden");
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
  const inputs = [...sorular[currentStep].querySelectorAll("input")];
  const allValid = inputs.every((input) => input.checkValidity());
  if (allValid) {
    currentStep += incrementor;
  }
  showCurrentStep();
});

function showCurrentStep() {
  sorular.forEach((step, index) => {
    console.log("Step---", step);
    if (index === currentStep) {
      step.classList.remove("hidden");
    } else {
      step.classList.add("hidden");
    }
  });
}

// Form radio control of the radio buttons!.

// Belirli sınıfa sahip div içindeki ul içindeki input etiketlerini seçmek
const inputs = document.querySelectorAll("#yanit ul li input");
const labels = document.querySelectorAll("#yanit ul li label");

inputs.forEach((input) => {
  input.classList.add("hidden", "peer");
});

labels.forEach((label) => {
  label.classList.add(
    "inline-flex",
    "items-center",
    "w-full",
    "px-5",
    "py-2",
    "text-gray-500",
    "bg-white",
    "border",
    "border-gray-200",
    "rounded-lg",
    "cursor-pointer",
    "dark:hover:text-gray-300",
    "dark:border-gray-700",
    "dark:peer-checked:text-blue-500",
    "peer-checked:border-blue-600",
    "peer-checked:text-blue-600",
    "hover:text-gray-600",
    "hover:bg-gray-100",
    "dark:text-gray-400",
    "dark:bg-gray-800",
    "dark:hover:bg-gray-700"
  );
});
