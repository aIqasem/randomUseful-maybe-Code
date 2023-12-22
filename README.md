<BR>

<img src="https://drive.google.com/uc?id=1Z_BDCjLPzBAtdVe-lVdfv5jfr3AnFvQw" alt="random image" width="70px" align="left"/>

> _From time to time i code some usefull ( for me ) or useless ( anyway ) stuff_<BR>
> _Guess what .. i upload here_

<BR>
<BR>

> For each python file you're gonna use ( which is not recommended ) .. create a ___function___ in your Powershell profile to run the file by typing the ___function___ name in the Powershell and pressing the magic Enter ( This should be waaay faster than running the python file via an IDE or remembering its path )

<BR>
<BR>

__〣__ ___Running these dumb functions from the Powershell___ ( _should be quicker_ )

- _open your Powershell, type .. to open your Powershell profile_<BR><BR>
  ```powershell
  start $profile
  ```
<BR>

- _Inside the file, add this anywhere_<BR><BR>
  ```powershell
    function some_memorable_name {
      python "path to python file of some useless function uploaded here"
    }
  ```
  
<BR>
<BR>

➥ &nbsp; _If &nbsp; `start $profile` &nbsp; didn't work, it's ok .. you are a cute person_<BR>
➦ &nbsp; _And a cute person searches for how to create a Powershell profile and put a function in_

<BR>
