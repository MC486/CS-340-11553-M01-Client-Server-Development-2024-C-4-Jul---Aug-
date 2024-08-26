# CS-340-11553-M01-Client-Server-Development-2024-C-4-Jul---Aug-

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

