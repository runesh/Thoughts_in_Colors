# Thoughts_in_Colors
This is a simple project where you can search for a keyword and based on the keywords the best possible color combinations would be returned and displayed in a masonry grid.

How are we doing it ? The keyword or phrase is searched in Bing images and the top 5 images are downloaded. Using K_Means clustering we are finding the top 3 colors from each images and based on the hex color code we label and assign background for each masonry grid


# To Run the project
1. Download both the folders
2. run command npm install inside GetColors_FE to install the node_modules
3. Then run ng serve to run the project locally in your browser at http://localhost:4200
4. For backend open the folder Flask_Colors and run command python app.py and it would start at http://127.0.0.1:5000
5. If you face any CORS issue kindly open chrome using disabled CORS chrome.exe --disable-web-security --disable-gpu --user-data-dir=~Temp

# Backend under the hood
1. We are using bing-image-downloader to download the images.
2. Using Opencv we are reading the downlaoded images
3. Then we are using K_Means clustering to find the 3 possible n_clusters for each image
4. Based on the clusters we find their hex color code and send them back.
5. We have packed all this using Flask API, where a simple get method will take in the query and return the hex codes in a list

# Frontend under the JS
1. Created an simple one page angular project
2. It has a input field to capture the keywords/phrases and on clicking the fetch color button we are sending the keywords to the API 
3. Based on the response we are setting the background of each Div with Hex color code 
4. We have used ngx-spinner for showing spinner/loader

**Note : Based on the internet and system speed it might take some time for the colors to be displayed


