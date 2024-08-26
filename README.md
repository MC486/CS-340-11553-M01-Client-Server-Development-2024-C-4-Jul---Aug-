# CS-340-11553-M01-Client-Server-Development-2024-C-4-Jul---Aug-

# How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

To write programs that are maintainable, readable, and adaptable, I focus on several key practices:

1. **Modular Design:** I break down the code into smaller, reusable modules that can be independently developed, tested, and maintained. The CRUD Python module from Project One is an example of this. By encapsulating the database interactions in a single module, I made it easier to manage and reuse the code.

2. **Consistent Naming Conventions:** I use meaningful and consistent naming conventions for variables, functions, and classes. This helps in making the code more readable and self-documenting, allowing others (or myself in the future) to understand the purpose of each component easily.

3. **Documentation and Comments:** I include comments to explain complex logic or decisions made in the code. In the CRUD module, I provided comments to clarify the purpose of specific database operations, which can be invaluable during future maintenance or updates.

4. **Error Handling:** Implementing robust error handling ensures that the program can gracefully handle unexpected situations without crashing. This adaptability is crucial in production environments where unexpected inputs or conditions are common.

The advantage of working with a modular CRUD Python module is that it abstracts the database operations from the main application logic. This separation of concerns allows the dashboard in Project Two to interact with the database seamlessly, without needing to know the specifics of the database queries. It also makes the module reusable in other projects where similar database interactions are required.

In the future, I could use this CRUD module as a template for interacting with other databases or even extend its functionality to support additional operations or more complex queries. By keeping the module well-documented and organized, it can be adapted to different contexts with minimal changes.

# How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

As a computer scientist, I approach problems methodically, starting with understanding the requirements and constraints. For the Grazioso Salvare project, I began by thoroughly analyzing the requirements for the dashboard and database, ensuring that I had a clear understanding of the client's needs. 

Once the requirements were clear, I broke the project down into smaller, manageable tasks. For example, I separated the development of the CRUD module from the creation of the dashboard. This allowed me to focus on each aspect individually, ensuring that each component was fully functional before integrating them.

Compared to previous assignments, this project required a more integrated approach, combining both backend (database) and frontend (dashboard) components. The challenge was to ensure that these components interacted seamlessly, providing a smooth user experience. I relied on techniques such as modular design, iterative testing, and regular validation against the project requirements to ensure that the solution met the client's needs.

In the future, when creating databases or other components to meet client requests, I would continue to use these strategies. Additionally, I would emphasize early and continuous communication with the client to ensure that the solution aligns with their expectations. Prototyping and iterative feedback loops can also be valuable in refining the solution throughout the development process.

# What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists design, develop, and optimize software and systems to solve complex problems and improve efficiency. This work is crucial in nearly every industry, as technology continues to be a driving force behind innovation and productivity.

In the case of the Grazioso Salvare project, my work on the dashboard and database helps the company streamline its process of identifying and training rescue dogs. By providing a user-friendly interface that allows staff to filter, visualize, and interact with the data, the dashboard makes it easier to make informed decisions quickly. This can lead to more efficient operations, better resource allocation, and ultimately, more successful rescue missions.

The impact of such a project extends beyond just the technical aspects. It enhances the company's ability to fulfill its mission, supports the staff in their daily tasks, and contributes to the overall success of the organization. In a broader sense, this project demonstrates how computer science can be applied to make a meaningful difference in the world, whether by improving business processes or, in this case, helping to save lives.





Grazioso Salvare Dashboard README
Project Overview
Grazioso Salvare is a rescue-animal training company that identifies dogs for search-and-rescue training. The company has collaborated with five animal shelters around Austin, Texas, to provide data on potential dogs. The goal of this project was to create a user-friendly web application dashboard that allows Grazioso Salvare to interact with and visualize data from a MongoDB database.
The dashboard was developed to allow seamless interaction with the MongoDB database. The data is stored and managed in MongoDB, while the user interface components, such as the data table and charts, provide dynamic visualizations and interactions. The custom Python CRUD module is utilized to handle database queries, ensuring smooth communication between the database and the dashboard interface.
Functional Requirements
The dashboard is designed to provide a user-friendly interface that allows users to interact with and visualize the data from MongoDB. It includes the following functionalities: 
1. Dashboard Branding
•	Grazioso Salvare Logo: The dashboard includes the Grazioso Salvare logo, which is a clickable link redirecting to the client's homepage: www.snhu.edu.
•	Unique Identifier: The dashboard displays a unique identifier, including the developer's name, "Michael Crevier," prominently at the top.
 
2. Interactive Filter Options
The dashboard includes radio buttons to filter the data based on the type of rescue Grazioso Salvare performs:
•	Water Rescue
 
•	Mountain Rescue

•	Disaster Rescue
 
•	Reset (Returns all widgets to their original, unfiltered state)
 
These options run queries on the MongoDB database and update the interactive data table, geolocation chart, and pie chart.

3. Interactive Data Table
The data table dynamically responds to the filtering options mentioned above. Additionally, users can:
•	Sort the table alphabetically by breed.
 
•	Filter the table by specific animal types (e.g., filtering by "Cat").

•	Adjust the number of rows displayed using a dropdown with options for 5, 10, 25, and 100 rows per page.

4. Geolocation Chart
The geolocation chart dynamically updates based on the selected filter and displays a marker for each animal. When a table entry is selected, the map marker automatically shows a popup with the animal's name and breed.
 
5. Pie Chart
The pie chart visualizes the distribution of animals by breed. Breeds with less than 2% representation are grouped under "All Other Breeds." The legend for the pie chart is displayed below the chart for clarity.
 
Tools and Technologies Used
MongoDB: Used as the database to store animal data.
Dash (Plotly): Framework used to create the web application dashboard.
Dash Leaflet: Used to create the interactive map in the dashboard.
Pandas: Used for data manipulation and analysis.
Python: Core programming language used for the CRUD operations and dashboard functionality.
Why MongoDB?
MongoDB was chosen as the model component of the development because it provides a flexible and scalable solution for storing and querying semi-structured data. Its integration with Python through the PyMongo driver allows for seamless CRUD operations, making it an ideal choice for this project.
Dash Framework
The Dash framework was chosen for its ability to create interactive and dynamic web applications with minimal overhead. Its integration with Plotly for data visualization and support for various UI components makes it suitable for building the dashboard required by Grazioso Salvare.
Steps Taken to Complete the Project
1.	Setting Up the Development Environment
Imported necessary Python packages.

Configured the ‘animal_shelter.py’ module to establish a connection to the MongoDB instance with the credentials:

2.	Data Import and Setup
Loaded the animal shelter data from the provided CSV file into the MongoDB database using the mongoimport command.

Verified the data was correctly inserted and accessible via the AnimalShelter class’s read method:

3.	Dashboard Layout and Design
Initialized the JupyterDash application and set up the basic layout of the dashboard.

Integrated the Grazioso Salvare logo with a URL link to the client's homepage:

4.	Implementing Interactive Filter Options
Developed radio buttons to filter data by rescue type, using the dcc.RadioItems component:

Implemented a callback function to update the data table and charts based on the selected filter:

5.	Building the Interactive Data Table
Configured the dash_table.DataTable component to allow for sorting, filtering, and pagination:

Implemented a dropdown to dynamically adjust the number of rows displayed in the table:

6.	Developing the Geolocation Chart
Used the Dash Leaflet library to create an interactive map that centers on the selected animal's location:

7.	Creating the Pie Chart

Implemented a callback to generate a pie chart of animal breeds, grouping breeds with less than 2% representation into "All Other Breeds":

8.	Testing and Debugging
Ran the dashboard locally to verify that all features worked as expected, especially the dynamic interaction between the filters, table, map, and chart.

Debugged issues related to MongoDB connection, data retrieval, and UI responsiveness.

9.	Final Review and Deployment
Conducted a final runthrough to ensure the dashboard met all client requirements, including branding and functionality.
Prepared the README with documentation and screenshots to showcase the dashboard’s functionality and deployment steps.
Reproduction Instructions
To reproduce the project, follow these steps:
1.	Clone the Repository: Ensure you have cloned the GitHub repository containing the project files.
2.	Install Required Packages:
 

3.	Set Up MongoDB:
o	Ensure your MongoDB server is running and accessible.
o	Update the connection parameters in the animal_shelter.py file with your MongoDB credentials.
4.	Run the Dashboard:
o	Launch Jupyter Notebook and open ProjectTwoDashboard.ipynb.
o	Execute the cells to start the Dash application.
5.	Testing the Dashboard:
o	Follow the scenarios mentioned in the screenshots to verify the dashboard's functionality.
o	Ensure all widgets update dynamically based on user interactions.

Challenges Encountered
Some challenges encountered during the development process included:
•	Configuring the correct callbacks to ensure that all widgets updated dynamically based on user input.
•	Optimizing the pie chart to group less frequent breeds under "All Other Breeds" to avoid cluttering the chart.
•	Ensuring compatibility between Dash Leaflet and the other Dash components for seamless integration.
These challenges were overcome by thorough testing and iterative development, ensuring that the final dashboard met all client requirements.

