# json-to-playjson
Converts JSON to Play framework JSON (https://www.playframework.com/documentation/2.2.x/api/scala/index.html#play.api.libs.json.JsValue)

## Why we wrote this script?
After developing any feature we need to write its backend tests, so we found ourselves spending too much time constructing the JSON for Play JSON. So this script converts normal JSON to how you would write it in the tests using Play JSON.

## How to use it?
```bash
python json_to_playjson.py '{"total":[17,17],"3":[0,0],"2":[0,0],"1":[17,17],"7":[0,0],"6":[0,0],"5":[0,0],"4":[0,0],"8":[0,0]}'
```

This will output on the stdout.

You might want to work with files if your json is big.
```bash
python json_to_playjson.py `cat test.json` > test.out
```

### Sample Output
```java
Json.obj() 
	.add("1", Json.arr() 
		.add(17)
		.add(17).build())
	.add("3", Json.arr() 
		.add(0)
		.add(0).build())
	.add("2", Json.arr() 
		.add(0)
		.add(0).build())
	.add("5", Json.arr() 
		.add(0)
		.add(0).build())
	.add("4", Json.arr() 
		.add(0)
		.add(0).build())
	.add("7", Json.arr() 
		.add(0)
		.add(0).build())
	.add("6", Json.arr() 
		.add(0)
		.add(0).build())
	.add("8", Json.arr() 
		.add(0)
		.add(0).build())
	.add("total", Json.arr() 
		.add(17)
		.add(17).build()).build()
```

Then you can use this in your tests like this.
```java
    @Test
    @LoadFixture(SampleFixture.class)
    public void sampleTest() {
        Result result = route(fakeRequest(GET, "/api/v1/sampleRoute"));
        assertThat(result).is(JSON_SUCCESS);
        JsValue expected = Json.obj() 
        	.add("1", Json.arr() 
        		.add(17)
        		.add(17).build())
        	.add("3", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("2", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("5", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("4", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("7", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("6", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("8", Json.arr() 
        		.add(0)
        		.add(0).build())
        	.add("total", Json.arr() 
        		.add(17)
        		.add(17).build()).build();

       assertThat(contentAsJson(result)).isEqualTo(expected);
    }
```


Enjoy testing :)


