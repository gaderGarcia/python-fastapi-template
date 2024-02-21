# python-fastapi-template
This project intends to have a folder structure and template for projects with Python and fastAPI.

The project uses FastAPI to expose a set of APIs using a router that handles the /transactions endpoints. This project uses middleware FastAPI to add response time for any incoming request.

The API /transactions/score?customer= uses internally the RQ library. This is to play and see how RQ library works for the parallelization of jobs.

The workers are running in docker using another project. This is because in Windows does not support fork() function. Due to that we created an external project to dockerize the worker
and help us to scale out.

The worker project and this application use an external library project that we created named rules. The rules project defines a simple function that we want to execute inside the workers.

- the fastAPI is invoked using /transactions/score?customer=vesta
- The application routes to transactions routes
- inside of the transactions calls background/enqueue_tasks folder
- inside of enqueue_tasks import rules project to use the calculate_score function
- this function creates 10 jobs to get a score, where each job can return a number between 0-20 minus the length of the customer name
- those jobs are sent to the workers using rq and Redis into the 'default' queue name.
- the workers are running in docker and executing the jobs, using the rules imported library.

  rules repo: https://github.com/gaderGarcia/dummy-rules
  rq-worker-docker: https://github.com/gaderGarcia/simple-rq-worker


![sequence-diagram](https://github.com/gaderGarcia/python-fastapi-template/assets/7773945/2606d52a-2f2b-4ce7-a097-9424ac9f092e)
