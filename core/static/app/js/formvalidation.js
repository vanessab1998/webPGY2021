$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "comentario"
  

  $("form[name='comentario']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      Documento: "required",
      pasaporte: {
        required: true,
        minlength: 8,
      },
      name: "required",
      ciudad: "required",
      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      comentario: {
        required: true,
        minlength: 50
      },
      
    },
    // Specify validation error messages
    messages: {
      Documento: "Selecciona un documento",
      pasaporte: "Ingresa tu numero de pasaporte",
      name: "Por favor ingresa tu nombre",
      ciudad: "Por favor ingresa tu ciudad",
      comentario: {
        required: "Por favor ingresa tu comentario",
        minlength: "Tu comentario debe tener al menos 50 caracteres"
      },
      email: {
        required:  "Por favor ingresa tu correo",
        email: "Por favor ingresa un correo válido"
      },
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });

});


