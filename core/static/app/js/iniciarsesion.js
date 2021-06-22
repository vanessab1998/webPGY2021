$(function() {
    
    $("form[name='iniciarsesion']").validate({
      rules: {
        email: {
          required: true,
          email: true
        },
        password: "required",
        
      },
      messages: {
        email: {
            required:  "Por favor ingresa tu correo",
            email: "Por favor ingresa un correo válido"
          },
        password: "Por favor ingresa tu contraseña",
       
      },
      submitHandler: function(form) {
        form.submit();
      }
    });
  
  });
  
  
  