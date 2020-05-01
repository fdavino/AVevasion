# AVevasion


##Configuration file template

```json
{
    "manipulations":{
        "template":"/abs/path/to/template",
        "payload":{
            "path":"/abs/path/to/payload",
            "specialch":"special character",
            "placeholder":"--!!--",
            "rate":0.1
        },
        "sub":[{
            "placeholder":"--!!!--",
            "str":"special character"
        }
        ]
    },
    "compilers":{
        "gcc":{
            "path":"/usr/bin/gcc",
            "options1":[{
                "name":"-o",
                "value":[
                    "hw.out"
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
            "options2":[{
                "name":"-o",
                "value":[
                    "hw2.out"
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


