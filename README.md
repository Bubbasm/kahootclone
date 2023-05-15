<p align="center">
  <img src="https://user-images.githubusercontent.com/55582807/236684094-4e2d0529-4b46-41d5-8ef8-09103b1030bd.png" />
</p>
<h1 align="center">
Manual de Usuario
</h1>

Este documento reúne el funcionamiento completo de la página creada en las prácticas 3 y 4 de PSI. Se explicará desde el registro de un usuario en la página hasta cómo jugar a los cuestionarios creados.

## 🔗 Enlaces a las páginas
Los enlaces a las páginas alojadas en render son los siguientes:

- Página principal: https://psi-p4-api.onrender.com

![image](https://user-images.githubusercontent.com/55582807/236681202-909f0cc6-1017-4e5c-8302-0eca57b9c95f.png)

- Página para unirse a un juego: https://psi-p4-vue.onrender.com

![image](https://user-images.githubusercontent.com/55582807/236681252-3f61b291-fc05-40f0-b475-0995c87d8e7b.png)

## 📌 Conceptos básicos
En la página principal, la __barra de navegación__ es la franja superior, y contiene el logotipo de la aplicación _KahootClone_, así como los botones de iniciar sesión, registrarse o cerrar sesión.

Para __volver a la página de inicio__, puede hacerse click en el logotipo de la aplicación en cualquier momento.

Durante el juego, los casos de empate se resuelven viendo __quién se unió antes al juego__.

## 👥 Manejo de los Usuarios
A no ser que se indique lo contrario, todas las acciones realizadas en esta sección se harán en la __página principal__ (enlace disponible en la sección _Enlaces a las páginas_).

### ➕ Registro
> _Para acceder al registro es necesario no haber iniciado sesión con otra cuenta. Si ya se ha iniciado sesión con otra cuenta se deberá cerrar sesión primero._
1. Hacer click en el botón azul de la barra de navegación (_Sign Up_). ![image](https://user-images.githubusercontent.com/55582807/236681778-542660d0-cf7b-4f42-ba67-c3a92936f7c9.png)
2. Rellenar los campos _Username_, _Password_ y _Password Confirmation_, siguiendo las instrucciones y restricciones que aparecen en la página.
3. Pulsar el botón _Sign Up_ que se encuentra en la parte inferior del formulario. Si hay algún error en el registro, se indicará en el propio formulario.
4. Tras un registro satisfactiorio, se redigirá al usuario a la página de inicio y se iniciará sesión automáticamente.

![image](https://user-images.githubusercontent.com/55582807/236681343-4406b4b4-7e87-4d9b-85fa-ed985f8ecf7d.png)


### ➡️ Inicio de Sesión
> _Para poder iniciar sesión es necesario haberse registrado anteriormente, y no haber iniciado sesión con otra cuenta. Si ya se ha iniciado sesión con otra cuenta se deberá cerrar sesión primero._
1. Hacer click en el botón verde de la barra de navegación (_Log In_). ![image](https://user-images.githubusercontent.com/55582807/236681843-c934e093-ff32-49b4-be60-5106e45410c8.png)
2. Rellenar los campos _Username_ y _Password_.
3. Pulsar el botón _Log In_ que se encuentra en la parte inferior del formulario. Si hay algún error en el inicio de sesión, se indicará en el propio formulario.
4. Tras un inicio de sesión satisfactorio, se redigirá al usuario a la página de inicio, que ahora mostrará opiciones para crear cuestionarios.

![image](https://user-images.githubusercontent.com/55582807/236681418-3713f894-c0f0-4752-9493-b53e440f7f2d.png)

### 👤 Comprobar usuario con el que se ha iniciado sesión
El nombre de usuario o _Username_ del usuario con el que se ha iniciado sesión aparecerá en la parte superior derecha de la página. ![image](https://user-images.githubusercontent.com/55582807/236681901-5e0a490e-6bc3-409a-b8cb-2476eb5856bc.png)

### ⬅️ Cerrar Sesión
> _Para poder cerrar sesión es necesario haber iniciado sesión anteriormente_
1. Hacer click en el botón rojo de la barra de navegación (_Log Out_).
4. Tras un cierre de sesión satisfactorio, se redigirá al usuario a la página de inicio. ![image](https://user-images.githubusercontent.com/55582807/236681928-573406b5-ce22-4972-9141-503577efd844.png)

## 📝 Edición de cuestionarios

### Crear un cuestionario
1. Desde la página de inicio, hacer click en el botón azul _Create a Questionnaire_. De forma alternativa puede accederse desde la página con el listado de cuestionarios. ![image](https://user-images.githubusercontent.com/55582807/236681952-beaf5404-f57c-4d65-8c20-3c641cb661a0.png)
2. Rellenar el campo _Title_ con el título del cuestionario.
3. Para finalizar la creación, hacer click en el botón verde _Submit_. Si se quiere cancelar la creación, hacer click en el botón rojo _Cancel_. Cualquier error en la creación se mostrará en el formulario.
4. Tras una creación exitosa, se redirigirá al usuario al listado de todos los cuestionarios creados.
![image](https://user-images.githubusercontent.com/55582807/236681990-df962f07-cadc-4b76-a769-4f96404406a4.png)

### 📃 Listar cuestionarios creados
1. Desde la página de inicio, hacer click en el botón con borde azul _All Questionnaires_.
![image](https://user-images.githubusercontent.com/55582807/236682024-593d3f30-c798-483a-ae4a-a19806df2449.png)

![image](https://user-images.githubusercontent.com/55582807/236682588-7a796ebe-a501-4fee-b592-7cf5045436b1.png)

### ✏️ Editar un cuestionario
1. Desde la lista de los cuestionarios creados, hacer click en el botón con borde amarillo _Edit_ correspondiente al cuestionario que se desea editar. Alternativamente, se puede pulsar el botón amarillo _Edit_ desde la página de detalles del cuestionario, situado al lado del nombre del cuestionario. ![image](https://user-images.githubusercontent.com/55582807/236682166-1c473815-8bdc-4d76-9408-46d934f9204f.png) ![image](https://user-images.githubusercontent.com/55582807/236682186-739b9152-5be0-4422-992f-9483bd6f20d5.png)
2. Modificar el título.
3. Para guardar las modificaciones del cuestionario, hacer click en el botón verde _Submit_. Si se quieren cancelar, hacer click en el botón rojo _Cancel_. Cualquier error en la modificación se mostrará en el formulario.
4. Tras una modificación exitosa, se redirigirá al usuario al listado de todos los cuestionarios creados.

![image](https://user-images.githubusercontent.com/55582807/236682389-0974f788-9054-46c1-93a4-b7b83a0bf7c3.png)

### ❌ Borrar un cuestionario
1. Desde la lista de los cuestionarios creados, hacer click en el botón con borde rojo _Delete_ correspondiente al cuestionario que se desea borrar. ![image](https://user-images.githubusercontent.com/55582807/236682415-1da33736-0fdc-47eb-a76a-bb0f94d8c6a7.png)
2. Se mostrará una página de confirmación, donde se debe pulsar el botón verde _Confirm_ para confirmar la elección, o el botón rojo _Cancel_ para volver atrás.
4. Tras borrar el cuestionario de forma exitosa, se redirigirá al usuario al listado de todos los cuestionarios creados.

![image](https://user-images.githubusercontent.com/55582807/236682441-cae79d19-4584-47d8-a16c-fe87a73f1716.png)


### 🔍 Acceder a los detalles de un cuestionario
1. Desde el listado de los cuestionarios creados, hacer click en el nombre del cuestionario al que se quiere acceder. De forma alternativa, si el cuestionario está entre los 5 últimos creados, se podrá acceder de la misma forma desde la página de inicio, ya que el cuestionario aparecerá en el listado _Your Latest Questionnaires_.

![image](https://user-images.githubusercontent.com/55582807/236683911-de1b4b41-f30e-4674-9f30-04fc961e7abb.png)

### ➕ Añadir preguntas a un cuestionario
1. Desde la página de detalles del cuestionario, hacer click en _Add question_, en la última fila de la tabla.
![image](https://user-images.githubusercontent.com/55582807/236682972-d55ad6c1-3293-4588-b54b-ba25725f1824.png)
3. Rellenar el campo _Question_ con el texto de la pregunta, y el campo _AnswerTime_ con el tiempo (en segundos) que un usuario tendrá para responder la pregunta.
4. Para finalizar la creación de la pregunta, hacer click en el botón verde _Submit_. Si se quiere cancelar la creación, hacer click en el botón rojo _Cancel_. Cualquier error en la creación se mostrará en el formulario.
5. Tras una creación exitosa, se redirigirá al usuario a la página de detalles del cuestionario.

![image](https://user-images.githubusercontent.com/55582807/236682995-11311275-5576-4ace-b210-634f2651f418.png)

### ✏️ Editar preguntas de un cuestionario
1. Desde la página de detalles del cuestionario, hacer click en el botón con borde amarillo _Edit_ correspondiente a la pregunta que se desea editar. Alternativamente, se puede pulsar el botón amarillo _Edit_ desde la página de detalles de la pregunta, situado al lado del nombre de la pregunta. ![image](https://user-images.githubusercontent.com/55582807/236682166-1c473815-8bdc-4d76-9408-46d934f9204f.png) ![image](https://user-images.githubusercontent.com/55582807/236682186-739b9152-5be0-4422-992f-9483bd6f20d5.png)
2. Modificar los campos que se deseen.
3. Para guardar las modificaciones de la pregunta, hacer click en el botón verde _Submit_. Si se quieren cancelar, hacer click en el botón rojo _Cancel_. Cualquier error en la modificación se mostrará en el formulario.
4. Tras una modificación exitosa, se redirigirá al usuario a la página de detalles del cuestionario.

![image](https://user-images.githubusercontent.com/55582807/236683402-7bf17bd5-3850-44a0-9f14-9109ca8283d1.png)

### ❌ Borrar preguntas de un cuestionario
1. Desde la página de detalles del cuestionario, hacer click en el botón con borde rojo _Delete_ correspondiente a la pregunta que se desea borrar. ![image](https://user-images.githubusercontent.com/55582807/236682415-1da33736-0fdc-47eb-a76a-bb0f94d8c6a7.png)
2. Se mostrará una página de confirmación, donde se debe pulsar el botón verde _Confirm_ para confirmar la elección, o el botón rojo _Cancel_ para volver atrás.
4. Tras borrar la pregunta de forma exitosa, se redirigirá al usuario a la página de detalles del cuestionario.

![image](https://user-images.githubusercontent.com/55582807/236683127-4edef205-e9da-42be-bddd-e04015308cf8.png)


### 🔍 Acceder a los detalles de una pregunta
1. Desde la página de detalles del cuestionario, hacer click en el nombre de la pregunta a la que se quiere acceder.

![image](https://user-images.githubusercontent.com/55582807/236683318-1599598a-de7f-41f4-a81d-e3ad4687704b.png)

### ➕ Añadir respuestas a una pregunta
1. Desde la página de detalles de una pregunta, hacer click en _Add answer_, en la última fila de la tabla. ![image](https://user-images.githubusercontent.com/55582807/236683164-8f224571-56bb-4d25-ae13-8210ea1e9dd8.png)
2. Rellenar el campo _Answer_ con el texto de la respuesta, y marcar si la respuesta es correcta o no en la casilla _Correct_.
> _El máximo número de respuestas a una pregunta es de 4. El botón de Add answer no se mostrará si se alcanza este número de respuestas._

> _El máximo número de respuestas correctas es 1._
3. Para finalizar la creación de la respuesta, hacer click en el botón verde _Submit_. Si se quiere cancelar la creación, hacer click en el botón rojo _Cancel_. Cualquier error en la creación se mostrará en el formulario.
4. Tras una creación exitosa, se redirigirá al usuario a la página de detalles de la pregunta.

![image](https://user-images.githubusercontent.com/55582807/236683239-37f8dddc-8f92-4793-9062-35f8947eb203.png)

### ✏️ Editar respuestas de una pregunta
1. Desde la página de detalles de una pregunta, hacer click en el botón con borde amarillo _Edit_ correspondiente a la respuesta que se desea editar. ![image](https://user-images.githubusercontent.com/55582807/236682166-1c473815-8bdc-4d76-9408-46d934f9204f.png)
2. Modificar los campos que se deseen.
3. Para guardar las modificaciones de la respuesta, hacer click en el botón verde _Submit_. Si se quieren cancelar, hacer click en el botón rojo _Cancel_. Cualquier error en la modificación se mostrará en el formulario.
4. Tras una modificación exitosa, se redirigirá al usuario a la página de detalles de una pregunta.

![image](https://user-images.githubusercontent.com/55582807/236683260-56e860fb-699f-4489-8919-8ce78bd0ae21.png)

### ❌ Borrar respuestas de una pregunta
1. Desde la página de detalles de una pregunta, hacer click en el botón con borde rojo _Delete_ correspondiente a la respuesta que se desea borrar. ![image](https://user-images.githubusercontent.com/55582807/236682415-1da33736-0fdc-47eb-a76a-bb0f94d8c6a7.png)
2. Se mostrará una página de confirmación, donde se debe pulsar el botón verde _Confirm_ para confirmar la elección, o el botón rojo _Cancel_ para volver atrás.
4. Tras borrar la respuesta de forma exitosa, se redirigirá al usuario a la página de detalles de la pregunta.

![image](https://user-images.githubusercontent.com/55582807/236683273-16e1a64e-0a07-45b5-8c90-b4be0a1fd8df.png)

## 🕹️ Jugar a los cuestionarios

### ➕ Crear un juego a partir de un cuestionario
> _Para crear un juego es necesario haber creado antes un cuestionario. Para una mejor experiencia, se recomienda que todas las preguntas de este tengan definidas las 4 respuestas, además de tener marcada la respuesta correcta. Aún así, la plataforma soporta preguntas con menor número de respuestas, o preguntas sin respuesta correcta._

1. Desde la página de detalles del cuestionario, hacer click en el botón verde _Play_. ![image](https://user-images.githubusercontent.com/55582807/236683958-34c70ef9-88b5-422b-97e3-e56fc7014fe8.png)
2. Se redirigirá a la página de juego, donde se dispondrá del código numérico (o pin) asociado al juego, además de la URL y el QR para conectarse como participante. También se mostrará un listado con los participantes que se vayan uniendo. Este listado se actualizará en tiempo real.
> _Es **muy importante** no actualizar esta página, ya que el código del juego cambiaría y se perderían todos los participantes, obligando a todos a unirse de nuevo._

![image](https://user-images.githubusercontent.com/55582807/236684713-1b4a5ce6-6471-443a-8055-c635d50a1aa0.png)

### ⤵️ Unirse a un juego
> _Para poder unirse a un juego es necesario haberlo creado antes._

> _Sólo se podrán unir participantes mientras el juego no haya comenzado._

> _El nombre o alias de los participantes es único._

#### Opción 1: unirse a través del enlace
1. Introducir el enlace https://psi-p4-vue.onrender.com en el navegador
2. Rellenar los campos con el _alias_ que se desee y el _pin_ del juego.
3. Hacer click en el botón verde _Join Game_.
4. Se redigirá al usuario a una página de espera, que se actualizará automáticamente cuando el juego comience.

#### Opción 2: escaneando el QR
1. Escanear el QR que se muestra en la pantalla del juego
2. Rellenar el campo _alias_ con el nombre que se desee. 
> _Nótese que el _pin_ del juego se rellena __automáticamente__._
3. Hacer click en el botón verde _Join Game_.
4. Se redigirá al usuario a una página de espera, que se actualizará automáticamente cuando el juego comience.

![image](https://user-images.githubusercontent.com/55582807/236685791-52bb162f-751a-4ed0-a7ef-f9f4112e3e10.png)

### 🎮 Proceso de juego
#### Punto de vista del creador del juego
1. Tras haber creado un juego, cuando el número de participantes sea el deseado se podrá iniciar el juego pulsando el botón verde _Launch Game_. ![image](https://user-images.githubusercontent.com/55582807/236684748-0294c958-04b1-49df-b5db-c5657d518d9c.png)
> _Cabe destacar que, tras hacer click en Launch Game, las páginas pueden ser actualizadas, y las cuentas atrás de las preguntas no se verán afectadas._
2. Se mostrará una cuenta atrás de 5 segundos.
![image](https://user-images.githubusercontent.com/55582807/236684776-6adc7e29-a13f-4b2f-9c08-cb0fffe28e7f.png)
3. Tras la cuenta atrás, se mostrarán la primera pregunta y las respuestas correspondientes. Cada una de las respuestas tendrá asociada un color y un símbolo. También se mostrará el tiempo restante para responder a la pregunta.
![image](https://user-images.githubusercontent.com/55582807/236684795-047c03c9-b9da-4164-ad91-d101a2246d0e.png)
4. Cuando pase el tiempo destinado a dicha pregunta, se resaltará la respuesta, y se mostrarán las puntuaciones de los participantes.
![image](https://user-images.githubusercontent.com/55582807/236684877-30349a8a-73d3-4f81-9d09-ffcb653e5a85.png)
Para pasar a la siguiente pregunta, pulsar el botón verde _Next question_. Si la pregunta que se muestra es la última, el botón será verde, pero dirá _Show Leaderboard_. ![image](https://user-images.githubusercontent.com/55582807/236684922-b6e96b46-c802-4beb-a9ef-3cc9d0d9d9eb.png) ![image](https://user-images.githubusercontent.com/55582807/236685585-00fabedf-ff1e-4710-a020-9ba348bd576d.png)
5. El proceso se repite hasta que no queden más preguntas, en cuyo caso se mostrarán las puntuaciones de todos y el _ranking_ final.
![image](https://user-images.githubusercontent.com/55582807/236685367-6c47b671-f1d9-4bf5-a16a-8de6112f8db7.png)


#### Punto de vista del participante
1. Tras haberse unido a un juego, se esperará hasta que el juego se inicie en la pantalla de espera
![image](https://user-images.githubusercontent.com/55582807/236685848-a6547576-79dd-4652-b034-cafaf5b25012.png)
2. Una vez se inicie el juego, se mostrarán tantos botones como respuestas tenga la pregunta que se muestra en la pantalla principal. Estos botones tendrán asociados los mismos colores y símbolos que la respuesta a la que corresponden.
![image](https://user-images.githubusercontent.com/55582807/236685902-1582c333-c856-45ad-9cf4-1a484a6b509a.png)
3. Se podrá pulsar uno de estos botones antes de que se acabe el tiempo de la pregunta. Si la respuesta ha sido registrada adecuadamente, se mostrará el texto _Answer registered_. Sino, se mostrará el error correspondiente.
![image](https://user-images.githubusercontent.com/55582807/236685929-feb52a61-e769-4af8-85d8-ce41309d1a87.png)
4. Cuando el creador del juego pase a la siguiente pregunta, la página se recargará automáticamente, repitiendo el proceso.
5. Al finalizar el juego, se redirigirá a los jugadores a la pantalla para unirse a un juego.
