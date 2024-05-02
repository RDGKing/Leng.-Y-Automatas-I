# Investigación sobre la Aplicación de Autómatas Finitos

En la teoría de la computación y la ingeniería en sistemas, los autómatas finitos son herramientas esenciales que se utilizan para modelar y abordar problemas complejos en múltiples disciplinas; desde aplicaciones en el diseño de circuitos electrónicos hasta sistemas de control. Su capacidad para representar el comportamiento de sistemas dinámicos los convierte en una herramienta importante en la investigación y la ingeniería.

## Ejemplo de aplicación en la vida real

### Elevador
Los sistemas de control de los elevadores son un ejemplo común de aplicación de autómatas finitos en la vida real. Estos sistemas se encargan de gestionar y modelar el comportamiento de los elevadores para transportar a las personas de manera correcta y segura entre diferentes pisos de acuerdo con las condiciones dadas.

### Funcionamiento del Sistema

1. **Entrada de Datos:** El sistema recibe información sobre la solicitud de los pasajeros, como los pisos de origen y destino, a través de los botones que el elevador proporciona.

2. **Modelado:** Se utiliza un autómata finito para modelar el comportamiento del elevador en función de las solicitudes recibidas y las condiciones actuales del sistema. El autómata puede tener diferentes estados que representan las acciones que el elevador puede realizar, como moverse hacia arriba o hacia abajo.

3. **Control del Elevador:** El autómata finito controla el movimiento y el comportamiento del elevador en tiempo real. Basándose en las entradas recibidas y el estado actual del sistema, el autómata determina la acción que debe realizar el elevador en cada momento. Por ejemplo, si se presiona el botón para detener el elevador desde un piso determinado, el autómata puede enviar la señal para que el elevador se detenga en el piso más cercano.

4. **Optimización del Movimiento:** Además de controlar el movimiento básico del elevador, el autómata finito también puede optimizar el comportamiento del sistema para minimizar el tiempo de espera de los pasajeros y mejorar la eficiencia del transporte.

### Control de Ascensores

#### Estados

- **Reposo:** El ascensor está en reposo, esperando una solicitud de subida o bajada.
- **Subiendo:** El ascensor se mueve hacia arriba en respuesta a una solicitud de subida.
- **Bajando:** El ascensor se mueve hacia abajo en respuesta a una solicitud de bajada.
- **Detenido:** El ascensor se detiene en un piso específico debido a una interrupción, priorizando llegar al piso más cercano.
- **Abrir:** Las puertas del ascensor se abren automáticamente al llegar al piso destino.
- **Cerrar:** Las puertas se cierran después de haber sido abiertas y se ha completado la solicitud.
- **Llegada:** El ascensor llega a un piso y se detiene.

#### Transiciones 

1. Cuando el ascensor está detenido, puede recibir solicitudes para dirigirse al piso solicitado y ofrecer sus servicios.

2. Después de abrir las puertas en el estado **Abrir**, el ascensor permanece detenido en el estado **Llegada** hasta que recibe la instrucción de cerrar las puertas **Cerrar**.

3. Desde el estado **Llegada**, el ascensor puede regresar al estado **Reposo** o continuar moviéndose si se recibe una nueva solicitud.

4. Desde el estado **Reposo**, el ascensor puede recibir solicitudes para subir o bajar.

5. Si se recibe una solicitud de subida, el ascensor pasa al estado **Subiendo** y continúa subiendo hasta llegar al piso deseado o recibir una solicitud de detención.

6. Si se recibe una solicitud de bajada, el ascensor pasa al estado **Bajando** y procede a bajar hasta llegar al piso deseado o recibir una solicitud de detención.

7. En el estado **Subiendo** o **Bajando**, si se recibe una solicitud de detención, el ascensor se detiene en el piso actual y pasa al estado **Detenido**.

### Diagrama de Control de Ascensores

![alt text](graphviz.png)