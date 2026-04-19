function loadDistricts() {
  const division = document.getElementById("division").value;
  const districtSelect = document.getElementById("district");

  districtSelect.innerHTML = '<option value=""> Select District </option>';
  
  
  const districts = {
    dhaka: [
      "Dhaka", "Gazipur", "Narayanganj", "Narsingdi",
      "Munshiganj", "Manikganj", "Tangail",
      "Kishoreganj", "Madaripur", "Gopalganj",
      "Rajbari", "Faridpur", "Shariatpur"
    ],

    chattogram: [
      "Chattogram", "Cox's Bazar", "Cumilla", "Feni",
      "Noakhali", "Lakshmipur", "Brahmanbaria",
      "Chandpur", "Khagrachhari", "Rangamati",
      "Bandarban"
    ],

    rajshahi: [
      "Rajshahi", "Bogura", "Pabna", "Sirajganj",
      "Natore", "Naogaon", "Joypurhat",
      "Chapainawabganj"
    ],

    khulna: [
      "Khulna", "Jessore", "Satkhira", "Bagerhat",
      "Narail", "Jhenaidah", "Magura",
      "Kushtia", "Chuadanga", "Meherpur"
    ],

    barishal: [
      "Barishal", "Bhola", "Patuakhali",
      "Pirojpur", "Jhalokathi", "Barguna"
    ],

    sylhet: [
      "Sylhet", "Moulvibazar",
      "Habiganj", "Sunamganj"
    ],

    rangpur: [
      "Rangpur", "Dinajpur", "Kurigram",
      "Gaibandha", "Nilphamari",
      "Lalmonirhat", "Panchagarh", "Thakurgaon"
    ],

    mymensingh: [
      "Mymensingh", "Jamalpur",
      "Netrokona", "Sherpur"
    ]
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
  function toggleCustomTime() {
  const timeSelect = document.getElementById("time");
  const customTimeDiv = document.getElementById("customtime");
  
  if (timeSelect.value == "custom") {
    customTimeDiv.style.display = "block";
  } else {
    customTimeDiv.style.display = "none";
  }
}

