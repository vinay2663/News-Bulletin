<?php

class MyDB extends SQLite3 {
    function __construct() {
       $this->open('project2.db');
    }
 }
$status = 'video';
$db2 = new MyDB();
    
    $sql2 =<<<EOF
    SELECT * from flag;
EOF;

    $ret2 = $db2->query($sql2);
    while($row = $ret2->fetchArray(SQLITE3_ASSOC) ) {
        $flag = $row['status'];
    }
if($flag != $status){
    if($flag == 'image'){
        header("Location: image.php"); 
      
      exit;
    }
    elseif ($flag == 'original'){
        header("Location: news.php"); 
      exit;
    }
}


?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="refresh" content="180">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Video</title>
  </head>
  <body>

  <div class="container">

           <div class="row">
           <div class="col-lg-11 col-sm-12">

        <marquee behavior="scroll" direction="left" style="font-family:Book Antiqua; font-size:35px; color: #FD0000"
            scrolldelay="25">
            Srinivas Institute of Technology</marquee>


        <marquee behavior="scroll" direction="right" style="font-family:Book Antiqua; font-size:26px; color: #2A69FD"
            scrolldelay="15">
            Electronics And Communication Engineering</marquee>

                <hr>
           </div> <!-- column ends-->

           <div class="col-lg-1 col-sm-12">

            <img src="Assets/images/logo1.jpg"
                                 width="100px" height="100px" alt="...">

           </div> <!-- column ends-->

        </div> <!-- row ends-->

        <div class="row">
            <div class="col-lg-12 col-sm-12">

           <iframe width="100%" height="540px" src="Assets/Uploads/videos/<?php
                      $db = new MyDB();
                            $sql =<<<EOF
                            SELECT * from video
                            EOF;

                            $ret = $db->query($sql);
                        while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
                            $video_name = $row['name'];
    }
                      echo $video_name;
                      $db->close()
                      ?>" frameborder="0" allowfullscreen></iframe>
                </iframe>

                <h4 style="color: #2A69FD;font-family:Times New Roman; font-size:24px; ">Description</h4>
                 <marquee behavior="scroll" direction="left" style="font-family:Algerian; font-size:24px; color: rgb(200,150,100);"
            scrolldelay="100">
           <?php
                          $db = new MyDB();
                            $sql =<<<EOF
                            SELECT * from video
                            EOF;

                            $ret = $db->query($sql);
                        while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
                            $video_des = $row['des'];
    }
                      echo $video_des;
                      $db->close()
                      ?>
        </marquee>

            </div> <!--- column ends -->
        </div> <!--- row ends -->

    </div> <!--- container ends -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>