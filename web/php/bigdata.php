<?php
// file handling with php
//written wed-jan-(17-1)-2019
$file = 'curated-full.tsv';
/* checking if the file exits */
if(file_exists($file)){
    //trying to open the file
    $openedFile = fopen($file, "r+");
    if($openedFile){
        $newFile = fopen("curatedCleaned.tsv", "w");
        while(!feof($openedFile)){
            $currentLine = fgets($openedFile);
            $lineWithoutFactoid = str_replace("factoid", " ", $currentLine);
            $lineWithoutNumber = str_replace(substr($lineWithoutFactoid, 0, 5), " ", $lineWithoutFactoid);
            if(fwrite($newFile, trim($lineWithoutNumber)."\n")){
                echo "OK";
            }
            echo "</br>";
        }
        fclose($newFile);
    }else{
        echo "unable to open file";
    }
    fclose($openedFile);
}else{
    echo "oops! file not found";
}