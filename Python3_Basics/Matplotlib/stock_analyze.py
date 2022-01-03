
from matplotlib import pyplot as plt

opening = [146.83999599999999, 146.190002, 144.0, 143.78999299999998, 143.03999299999998, 144.279999, 144.850006, 144.25, 144.429993, 147.33999599999999, 143.369995, 140.300003, 141.389999, 143.610001, 147.46000700000002, 151.529999, 150.600006, 152.71000700000002, 151.91000400000001, 155.759995, 156.28999299999998, 155.58999599999999, 158.550003, 156.550003, 156.100006, 157.820007, 160.330002, 159.110001, 160.25, 160.5, 158.08999599999999, 153.610001, 156.149994, 157.860001, 157.75, 158.350006, 161.0, 162.83999599999999, 163.600006, 163.610001, 163.520004, 163.419998, 165.490005, 164.949997, 165.600006, 166.119995, 166.270004, 155.300003, 154.380005, 154.33999599999999, 149.440002, 151.449997, 154.28999299999998, 153.679993, 152.5, 155.130005, 155.009995, 158.779999, 156.619995, 151.639999, 152.820007, 149.759995, 149.800003, 146.580002, 146.130005, 146.649994, 150.33999599999999, 152.369995, 155.770004, 158.509995, 159.300003, 162.91000400000001, 176.119995, 182.970001, 183.83999599999999, 182.720001, 188.690002, 187.78999299999998, 187.699997, 189.889999, 182.0, 184.259995, 182.490005, 182.220001, 180.529999, 179.600006, 181.0, 181.369995, 171.429993, 174.029999, 169.860001, 169.800003, 171.529999, 167.5, 169.229996, 165.949997, 166.91000400000001, 167.759995, 168.350006, 169.860001, 168.580002, 166.429993, 165.0, 169.5, 175.449997, 175.550003, 173.399994, 175.25, 178.800003, 178.449997, 178.100006, 182.550003, 184.070007, 183.25, 182.729996, 183.610001, 184.979996, 186.100006, 185.820007, 188.399994, 186.46000700000002, 180.699997, 181.009995, 181.25, 180.729996, 182.110001, 177.649994, 181.41000400000001, 185.649994, 194.300003, 199.100006, 197.850006, 195.570007, 196.75, 199.699997, 201.949997, 200.110001, 199.990005, 193.009995, 195.899994, 194.169998, 192.75, 195.380005, 194.66000400000001, 197.199997, 199.619995, 198.21000700000002, 197.240005, 197.449997, 199.800003, 200.0, 200.0, 196.0, 194.46000700000002, 191.610001, 191.119995, 193.639999, 194.53999299999998, 194.330002, 195.740005, 193.300003, 195.03999299999998, 196.580002, 196.649994, 195.559998, 195.33999599999999, 198.91000400000001, 190.309998, 186.990005, 189.360001, 183.5, 183.380005, 185.71000700000002, 186.5, 187.850006, 186.009995, 186.100006, 187.979996, 189.610001, 191.199997, 190.179993, 187.940002, 189.440002, 188.330002, 189.779999, 187.800003, 187.179993, 192.509995, 196.100006, 202.050003, 206.199997, 207.25, 210.020004, 212.11000099999998, 207.570007, 214.289993, 217.17999300000002, 224.24000499999997, 221.0, 220.33999599999999, 222.75, 222.0, 255.05000299999998, 250.88000499999998, 263.0, 271.48999, 274.200012, 277.0, 281.940002, 266.410004, 263.0, 262.0, 247.69999700000002, 266.579987, 267.079987, 253.850006, 252.13999900000002, 257.290009, 260.47000099999997, 270.02999900000003, 278.730011, 277.73999, 282.070007, 283.880005, 281.0, 288.75, 294.769989, 293.100006, 292.75, 284.649994, 302.850006, 319.880005, 320.0, 322.200012, 321.329987, 333.559998, 323.869995, 318.160004, 323.170013, 321.420013, 315.799988, 313.26001, 316.350006, 313.070007, 307.410004, 309.359985, 322.48999, 298.390015, 287.0, 291.940002, 285.450012, 273.630005]

close = [145.5, 143.619995, 143.740005, 143.110001, 143.850006, 144.350006, 143.830002, 142.919998, 147.25, 143.360001, 139.759995, 141.179993, 142.869995, 143.830002, 152.16000400000001, 150.169998, 153.080002, 152.199997, 155.350006, 156.449997, 155.58999599999999, 157.25, 156.600006, 156.380005, 157.46000700000002, 160.279999, 158.53999299999998, 160.809998, 160.020004, 159.41000400000001, 153.199997, 155.699997, 157.020004, 157.16000400000001, 157.949997, 157.75, 163.050003, 162.429993, 163.220001, 163.070007, 162.990005, 165.179993, 165.059998, 165.169998, 165.610001, 165.880005, 158.029999, 151.440002, 152.720001, 152.199997, 151.759995, 152.380005, 153.399994, 152.050003, 155.029999, 154.889999, 158.020004, 157.5, 151.029999, 153.41000400000001, 150.08999599999999, 149.41000400000001, 146.169998, 147.610001, 146.25, 150.179993, 152.669998, 154.330002, 158.75, 158.21000700000002, 161.119995, 161.699997, 183.600006, 183.860001, 183.600006, 188.53999299999998, 187.91000400000001, 186.970001, 189.080002, 182.679993, 184.03999299999998, 181.66000400000001, 182.029999, 180.740005, 179.229996, 180.270004, 181.330002, 178.360001, 175.779999, 169.139999, 171.399994, 171.0, 168.5, 169.979996, 166.08999599999999, 166.53999299999998, 166.759995, 169.33999599999999, 169.059998, 168.130005, 165.949997, 167.119995, 168.809998, 174.690002, 174.71000700000002, 174.740005, 174.520004, 179.25, 179.0, 176.419998, 181.740005, 185.149994, 183.639999, 182.630005, 182.350006, 184.619995, 185.679993, 185.509995, 188.779999, 187.350006, 178.550003, 179.380005, 181.970001, 180.699997, 181.350006, 177.009995, 179.190002, 184.449997, 194.389999, 198.020004, 196.869995, 195.080002, 194.949997, 195.860001, 199.490005, 202.679993, 199.479996, 195.53999299999998, 195.130005, 194.16000400000001, 192.470001, 196.020004, 193.770004, 195.21000700000002, 199.53999299999998, 198.369995, 196.429993, 198.0, 199.320007, 200.009995, 200.130005, 195.889999, 196.440002, 193.899994, 192.020004, 195.080002, 195.71000700000002, 192.119995, 195.509995, 193.199997, 194.100006, 196.229996, 196.320007, 195.75, 195.050003, 199.179993, 188.149994, 187.580002, 186.820007, 184.03999299999998, 184.21000700000002, 185.300003, 185.199997, 188.53999299999998, 186.220001, 185.729996, 187.860001, 189.559998, 190.119995, 190.419998, 187.020004, 188.820007, 188.619995, 189.940002, 187.759995, 186.240005, 192.71000700000002, 191.96000700000002, 201.070007, 205.050003, 205.630005, 209.99000499999997, 212.05000299999998, 209.309998, 212.520004, 217.24000499999997, 221.229996, 221.52999900000003, 217.5, 220.330002, 220.460007, 227.580002, 250.289993, 261.299988, 269.700012, 274.600006, 284.589996, 278.799988, 270.299988, 265.070007, 267.429993, 254.25999500000003, 265.72000099999997, 264.559998, 250.100006, 249.47000099999997, 257.950012, 258.269989, 266.0, 280.269989, 278.519989, 278.549988, 281.040009, 278.140015, 285.929993, 294.160004, 290.609985, 291.380005, 290.390015, 301.049988, 315.0, 325.22000099999997, 321.160004, 317.0, 331.440002, 321.299988, 315.880005, 321.549988, 321.089996, 318.450012, 313.480011, 317.5, 316.480011, 306.700012, 300.940002, 320.350006, 300.690002, 285.769989, 295.350006, 280.290009, 283.670013, 287.629211]

business_days= range(252)

# Add code here
plt.plot(business_days, opening)
plt.plot(business_days, close)
plt.xlabel("Stock Exchange Days for Past Year")
plt.ylabel("Price")
plt.title("Netflix Stock Prices for 2017")
legend_labels = ["Opening Price", "Closing Price"]
plt.legend(legend_labels, loc=8)
plt.show()