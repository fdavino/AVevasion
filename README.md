# AVevasion


##Configuration file template

### obligatory		! !
### optional		- -

```json
{
    "info":{
        "inputFile":"ABSOLUTE PATH OF INPUT FILE",  #!! (absolute path)
        "programLanguage":"c"    					#--
    },
    "compilers":{
        "gcc":{  									##!! (name of compilation test)
            "path":"/usr/bin/gcc", 					##!! (absolute path)
            "options1":[{ 							##-- (option befor input file)
                "name":"-o",						##!!
                "value":[							##-- 
                    "hw.out"						## (1 or more)
                    ]
                  },
                {
                "name":"-c"
                }]            
        },
        "g++":{
            "path":"/usr/bin/g++",
            "options1":[{
                "name":"-c"
            }],
            "options2":[{							##-- (option after input file)
                "name":"-o",						##!!
                "value":[							##--
                    "hw2.out"						## (1 or more)
                    ]                               
                }
            ]            
        },
        "clang":{
            "path":"/usr/bin/clang",
            "options2":[{
                "name":"-o",
                "value":[
                    "hw3.out"
                    ]                               
                }
            ]            
        }    
    }

}

```