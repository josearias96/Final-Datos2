# Final-Datos2
Entrega final del proyecto de datos 2 UFM

Para el proyecto final de la clase de Datos 2 se creó un sistema de búsqueda de datos a 3 diferentes APIs.

Para el proyecto escojí los siguientes apis:
  - Twitter
  - NewsApi
  - New York Times
  
El sistema fue creado a base de Python. Se creo un API endpoint que recibía consultas a base de 2 keywords y un token de usuario. El sistema hace un GET request a una base de datos de Google Firestore. En el cual consulta si el usuario existe y si se ha hecho alguna otra consulta con alguna de esas 2 keywords. El sistema es de alta disponibilidad por lo que responde rapidamente si encuentra algun resultado en la base de datos. Si no encuentra nada, el sistema consulta a las 3 APIs definidas para dar una respuesta al usuario. Se utilizó una estrategia de Multithreading de Python (libreria) para acelerar el proceso de consulta a los endpoints. Por lo que el thread que responda primero es el primero devuelto al usuario. 
Para la visualización de las consultas al endpoint creado, se utilizó Elastic Stack. El sistema de python genera un log que alimenta a Logstash, quien alimenta a Elasticsearch y a Kibana respectivamente para la visualización de las búsquedas. 

Se utilizó una máquina local para servir el ELK Stack y Python fue servido con Flask.
