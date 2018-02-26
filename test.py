#coding=utf-8
import random,base64
def encrypt(some):	
	cryptedstr=""
	test=""
	for i in range(len(some)):
		print random.randint(0,255)
		temp=ord(some[i:i+1])^random.randint(0,255)
		test=str(temp)
		while len(test)<3:
			test = '0'+test
		cryptedstr=cryptedstr+test
		$cryptedstr .= $temp. "";
	print cryptedstr	
	return base64.b64encode(cryptedstr)
print encrypt("Admin")
	# function decrypt ($str)
	# {
	# 	srand(3284724);
	# 	if(preg_match('%^[a-zA-Z0-9/+]*={0,2}$%',$str))
	# 	{
	# 		$str = base64_decode($str);
	# 		if ($str != "" && $str != null && $str != false)
	# 		{
	# 			$decStr = "";
				
	# 			for ($i=0; $i < strlen($str); $i+=3)
	# 			{
	# 				$array[$i/3] = substr($str,$i,3);
	# 			}

	# 			foreach($array as $s)
	# 			{
	# 				$a = $s ^ rand(0, 255);
	# 				$decStr .= chr($a);
	# 			}
				
	# 			return $decStr;
	# 		}
	# 		return false;
	# 	}
	# 	return false;
	# }