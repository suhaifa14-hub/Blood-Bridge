function loadCurrentDistricts() {
  const division = document.getElementById("current-division").value;
  const districtSelect = document.getElementById("current-district");

  districtSelect.innerHTML = '<option value=""> Select District </option>';

  const districts = {
    dhaka: ["Dhaka", "Gazipur", "Narayanganj", "Narsingdi", "Munshiganj", "Manikganj", "Tangail", "Kishoreganj", "Madaripur", "Gopalganj", "Rajbari", "Faridpur", "Shariatpur"],
    chattogram: ["Chattogram", "Cox's Bazar", "Cumilla", "Feni", "Noakhali", "Lakshmipur", "Brahmanbaria", "Chandpur", "Khagrachhari", "Rangamati", "Bandarban"],
    rajshahi: ["Rajshahi", "Bogura", "Pabna", "Sirajganj", "Natore", "Naogaon", "Joypurhat", "Chapainawabganj"],
    khulna: ["Khulna", "Jessore", "Satkhira", "Bagerhat", "Narail", "Jhenaidah", "Magura", "Kushtia", "Chuadanga", "Meherpur"],
    barishal: ["Barishal", "Bhola", "Patuakhali", "Pirojpur", "Jhalokathi", "Barguna"],
    sylhet: ["Sylhet", "Moulvibazar", "Habiganj", "Sunamganj"],
    rangpur: ["Rangpur", "Dinajpur", "Kurigram", "Gaibandha", "Nilphamari", "Lalmonirhat", "Panchagarh", "Thakurgaon"],
    mymensingh: ["Mymensingh", "Jamalpur", "Netrokona", "Sherpur"]
  };

  if (division !== "") {
    districts[division].forEach(district => {
      const option = document.createElement("option");
      option.value = district;
      option.text = district;
      districtSelect.add(option);
    });
  }
}


 function toggleDate(show) {
  const dateField = document.getElementById("dateField");
  const dateInput = document.getElementById("donation_date");

  if (show) {
    dateField.style.display = "block";
    dateInput.required = true;
  } else {
    dateField.style.display = "none";
    dateInput.required = false;
    dateInput.value = "";
  }
}

