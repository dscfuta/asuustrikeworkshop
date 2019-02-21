<?php
namespace App\File;

class fileController
{
    var $error = "";
    public static function openFile($path, $mode){
        if(file_exists($path)){
            # continue
            return fopen($path, $mode);
        } else {
            # return error
            self::error('file not found');
        }
    }
    public static function readFile($file){
        while(!feof($file)){
            $currentLine = fgets($openedFile);
            $lineWithoutFactoid = str_replace("factoid", " ", $currentLine);
            $lineWithoutNumber = str_replace(substr($lineWithoutFactoid, 0, 5), " ", $lineWithoutFactoid);
            if(fwrite($newFile, trim($lineWithoutNumber)."\n")){
                echo "OK";
            }
            echo "</br>";
        }
    }
}

