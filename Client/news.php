<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('project2.db');
      }
   }

   $status = 'original';
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
       elseif ($flag == 'video'){
           header("Location: video.php"); 
         exit;
       }
   }
   
   $db = new MyDB();
  
   $sql =<<<EOF
   SELECT * from image;
EOF;

function check_blank($key) {
    if($key=="")
    return TRUE;
    else
    return FALSE;
}

$image_array = array();
$des = array();
$pdf_name;
$video_name;


$ret = $db->query($sql);
while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
    if(!check_blank($row['name']))
    array_push($image_array,$row['name']);

    if(!check_blank($row['description']) )
        array_push($des,$row['description']);
}
$db->close()

?>

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="refresh" content="180">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>News Bulletin</title>
</head>

<body>
    <div class="container">
        <div class="row">
           <div class="col-lg-11 col-sm-11">

        <marquee behavior="scroll" direction="left" style="font-family:Book Antiqua; font-size:35px; color: #FD0000"
            scrolldelay="25">
            Srinivas Institute of Technology</marquee>


        <marquee behavior="scroll" direction="right" style="font-family:Book Antiqua; font-size:26px; color: #2A69FD"
            scrolldelay="15">
            Electronics And Communication Engineering</marquee>

                <hr>
           </div> <!-- column ends-->

           <div class="col-lg-1 col-sm-1">

            <img src="Assets/images/logo1.jpg"
                                 width="100px" height="100px" alt="...">

           </div> <!-- column ends-->

        </div> <!-- row ends-->

           <div class="row">
            
            <div class="col-lg-4 col-sm-12">
                <center>
               <h4 style="color:rgb(27,11,206);">Images</h4>
                </center>
                <hr>

      <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="3"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="4"></li>
    <li data-target="#carouselExampleCaptions" data-slide-to="5"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">

    <img src="Assets/Uploads/images/<?php  echo $image_array[count($image_array)-1];?>"
         class="d-block w-100" width="100%" height="350px" alt="...">

      <div class="carousel-caption d-none d-md-block">
      <h4><?php  echo $des[count($des)-1];?></h4>
      </div>
    </div>
    <div class="carousel-item">

    <img src="Assets/Uploads/images/<?php  echo $image_array[count($image_array)-2];?>"
         class="d-block w-100" width="100%" height="350px" alt="...">

      <div class="carousel-caption d-none d-md-block">
        <h4><?php  echo $des[count($des)-2];?></h4>
      </div>
    </div>
    <div class="carousel-item">

     <img src="Assets/Uploads/images/<?php  echo $image_array[count($image_array)-3];?>"
         class="d-block w-100" width="100%" height="350px" alt="...">

     <div class="carousel-caption d-none d-md-block">
     <h4><?php  echo $des[count($des)-3];?></h4>
      </div>
    </div>

    <div class="carousel-item">

        <img src="Assets/Uploads/images/<?php  echo $image_array[count($image_array)-4];?>"
            class="d-block w-100" width="100%" height="350px" alt="...">

            <div class="carousel-caption d-none d-md-block">
                 <h4><?php  echo $des[count($des)-4];?></h4>
            </div>
     </div>

     <div class="carousel-item">

        <img src="Assets/Uploads/images/<?php  echo $image_array[count($image_array)-5];?>"
            class="d-block w-100" width="100%" height="350px" alt="...">

            <div class="carousel-caption d-none d-md-block">
                 <h4><?php  echo $des[count($des)-5];?></h4>
            </div>
     </div>

     <div class="carousel-item">

        <img src="Assets/Uploads/images/<?php  echo $image_array[count($image_array)-6];?>"
            class="d-block w-100" width="100%" height="350px" alt="...">

            <div class="carousel-caption d-none d-md-block">
                 <h4><?php  echo $des[count($des)-6];?></h4>
            </div>
         </div>

            </div>
            <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
            </div>

            </div> <!-- column ends -->

            <div class="col-lg-5 col-sm-12">
               <center>
               <h4 style="color:rgb(27,11,206);">Circular</h4>
                </center>
                <hr>
                <embed src="Assets/Uploads/pdf/<?php
                    $db = new MyDB();
                        $sql =<<<EOF
                        SELECT * from pdf
                        EOF;

                        $ret = $db->query($sql);
                    while($row = $ret->fetchArray(SQLITE3_ASSOC) ) 
                        $pdf_name = $row['name'];  echo $pdf_name ; 
                         $db->close() 
                          ?>#toolbar=0&navpanes=0&scrollbar=0" type="application/pdf" width="100%" height="400px" />

            </div> <!-- column ends -->

            <div class="col-lg-3 col-sm-12" >

              <center>
               <h4 style="color:rgb(27,11,206);">Videos</h4>
                </center>

                <hr>

                <iframe width="400" height="320" src="Assets/Uploads/videos/<?php
                        $db = new MyDB();
                            $sql =<<<EOF
                            SELECT * from video
                            EOF;

                            $ret = $db->query($sql);
                        while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
                            $video_name = $row['name'];
}
                      echo $video_name;
                      $db->close() ?>" frameborder="0" allowfullscreen></iframe>
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

            </div> <!-- column ends -->

        </div> <!-- row ends -->

        <div class = "row" >
          <div class = "col-lg-12 col-sm-12">
            <hr>
            <h3 style="color:rgb(255,0,0);"> Flash News</h3>
              <marquee behavior="scroll" direction="left" style="font-family:Book Antiqua; font-size:26px; color: #2A69FD"
            scrolldelay="15">
             <?php $data = file_get_contents("Assets/Uploads/circular.txt");
                        echo ($data);  ?></marquee>

          </div> <!-- column ends-->
          
        </div> <!-- row ends-->

    </div> <!-- container ends -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
        crossorigin="anonymous"></script>
</body>

</html>
