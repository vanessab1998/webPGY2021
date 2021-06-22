$(function() {
    $("form[name='registro']").validate({
      rules: {
        name: "required",
        rut: "required",
        ciudad: "required",
        email: {
            required: true,
            email: true
          },
        telefono: "required",
        password: "required",
      },
      messages: {
        name: "Por favor ingresa tu nombre",
        rut: "Por favor ingresa tu rut",
        ciudad: "Por favor ingresa tu ciudad",
        email: {
          required:  "Por favor ingresa tu correo",
          email: "Por favor ingresa un correo válido",
        },
        telefono:"Ingresa tu numero de telefono",
        password:"Por favor ingresa tu contraseña",
      },
      submitHandler: function(form) {
        form.submit();
      }
    });
  
  });
  
  
  