$(function(){


    $.validator.addMethod('strongPassword', function(value, element) {
        return this.optional(element) 
            || value.length >= 8 
            && /\d/.test(value)
            && /[a-z]/i.test(value);
    }, 'La contraseña debe tener al menos  8 carácteres de largo, contener un número y una letra\.')

    $("#formulario-registro").validate({
        errorClass: "error-red",
        
        rules:{
            txtNombre:{
                required: true,
                minlength: 3
            },
            txtEmail:{
                required: true,
                email: true
            },
            txtTelefono:{
                required: true,
                minlength: 9,
                maxlength: 9
            },
            txtDireccion:{
                required: true,
                minlength: 10,
                maxlength: 50
            },
            txtContrasena:{
                required: true,
                maxlength: 26,
                strongPassword: true
            },
            txtrContrasena:{
                required:true,
                equalTo: "#txtContrasena"
            }
        },
        
        messages:{
            txtNombre:{
                required: "El nombre es obligatorio\.",
                minlength: "El largo mínimo del nombre es de 3 carácteres\."
            },
            txtEmail:{
                required: "El correo es obligatorio\.",
                email: "El email es inválido"
            },
            txtTelefono:{
                required: "Ingresa tu número",
                minlength: "El número debe tener al menos 9 dígitos\.",
                maxlength: "El número no puede exceder los 9 dígitos\." 
            },
            txtDireccion:{
                required: "Ingresa tu dirección",
                minlength: "La dirección debe tener al menos 10 carácteres\.",
                maxlength: "La dirección no puede superar los 50 carácteres\."
            },
            txtContrasena:{
                required: "Ingresa una contraseña\.",
                maxlength: "La contraseña no puede superar los 26 carácteres\."

            },
            txtrContrasena:{
                required: "Vuelve a ingresar tu contraseña\.",
                equalTo: "La contraseña no coincide\."
            }

        },

    });
});

