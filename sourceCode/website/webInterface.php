<!DOCTYPE html> 
<html>
<head>
<meta charset="UTF-8">
<title>jQuery Mobile Web App</title>
<link href="http://code.jquery.com/mobile/1.3.0/jquery.mobile-1.3.0.min.css" rel="stylesheet" type="text/css"/>
<script src="http://code.jquery.com/jquery-1.8.3.min.js" type="text/javascript"></script>
<script src="http://code.jquery.com/mobile/1.3.0/jquery.mobile-1.3.0.min.js" type="text/javascript"></script>
</head> 
<body> 

<div data-role="page" id="page">
	<div data-role="header">
		<h1>Page One</h1>
	</div>
	<div data-role="content">	
		<ul data-role="listview">
			<li><a href="#page2">Page Two</a></li>
            <li><a href="#page3">Page Three</a></li>
			<li><a href="#page4">Page Four</a></li>
		</ul>		
	</div>
	<div data-role="footer">
		<h4>Page Footer</h4>
	</div>
</div>

<div data-role="page" id="page2">
	<div data-role="header">
		<h1>Add an Alarm</h1>
	</div>
	<div data-role="content">
	  <p>
	  <div data-role="fieldcontain">
		  <p>
		    <label for="time">Time:<br>
		    </label>
		    <input type="time" name="time" id="time" value=""  />
	    </p>
	  </div>
      <div data-role="fieldcontain">
        <p>
          <label for="date">Date:</label>
        </p>
        <p>
          <input type="date" name="date" id="date" value=""  />
        </p>
        <div data-role="fieldcontain">
          <p>
            <label for="textinput">Text Input:</label>
          </p>
          <p>
            <input type="text" name="textinput" id="textinput" value=""  />
          </p>
        </div>
        </p>
      <a href="#" data-role="button">Button</a></div>
      Content
</p>
		<p>&nbsp;</p>
	</div>
	<div data-role="footer">
		<h4>Page Footer</h4>
	</div>
</div>

<div data-role="page" id="page3">
	<div data-role="header">
		<h1>Page Three</h1>
	</div>
	<div data-role="content">
	  <div data-role="fieldcontain"><div data-role="fieldcontain">
        <label for="textinput2">Preset 1:</label>
	      <input type="text" name="textinput2" id="textinput2" value=""  />
        </div>
	    </p>
	  </div>
	</div>
	<div data-role="content">
	  <div data-role="fieldcontain"><div data-role="fieldcontain">
        <label for="textinput3">Preset 2:</label>
	      <input type="text" name="textinput2" id="textinput2" value=""  />
        </div>
	    </p>
	  </div>
	</div>
 			<div data-role="content">
	  <div data-role="fieldcontain"><div data-role="fieldcontain">
        <label for="textinput4">Preset 3:</label>
	      <input type="text" name="textinput2" id="textinput2" value=""  />
        </div>
	    </p>
	  </div>
	</div>
    	<div data-role="content">
	  <div data-role="fieldcontain"><div data-role="fieldcontain">
        <label for="textinput5">Preset 4:</label>
	      <input type="text" name="textinput2" id="textinput2" value=""  />
        </div>
	    </p>
	  </div>
	</div>
    	<div data-role="content">
	  <div data-role="fieldcontain"><div data-role="fieldcontain">
        <label for="textinput6">Preset 5:</label>
	      <input type="text" name="textinput2" id="textinput2" value=""  />
        </div>
	    </p>
	  </div>
	</div>
        	<div data-role="content">
	  <div data-role="fieldcontain"><div data-role="fieldcontain">
        <label for="textinput7">Preset 6:</label>
	      <input type="text" name="textinput2" id="textinput2" value=""  />
        </div>
	    </p>
	  </div>
	</div>      
	<div data-role="footer">
		<h4>Page Footer</h4>
	</div>
</div>

<div data-role="page" id="page4">
	<div data-role="header">
		<h1>Active Alarms</h1>
	</div>
	<div data-role="content">	
		<?php
$con=mysqli_connect("localhost","root","root","alarmDB");
// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT * FROM Persons");

echo "<table border='1'>
<tr>
<th>Firstname</th>
<th>Lastname</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['FirstName'] . "</td>";
echo "<td>" . $row['LastName'] . "</td>";
echo "</tr>";
}
echo "</table>";

mysqli_close($con);
?>
	</div>
	<div data-role="footer">
		<h4>Page Footer</h4>
	</div>
</div>

</body>
</html>
