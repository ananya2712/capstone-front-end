import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import os

weighted = [[3499, 1217, 818, 2449, 343, 296, 356, 1, 2599, 56949],
 [351, 1754, 2065, 5192, 611, 480, 296, 780, 3897, 2420],
 [4925, 3499, 2335, 4673, 2381, 296, 356, 1, 1287, 5349],
 [4925, 3499, 3548, 3165, 3267, 296, 480, 318, 913, 1591],
 [4925, 3499, 2335, 1011, 2077, 296, 480, 318, 8376, 1264],
 [4925, 3499, 2335, 2371, 5077, 296, 480, 1, 502, 1527],
 [4929, 4925, 3499, 612, 3646, 296, 318, 1, 2599, 2116],
 [4925, 4929, 3499, 876, 45361, 296, 318, 480, 4235, 2019],
 [4925, 4929, 4614, 2982, 3908, 480, 2858, 1, 5620, 1682],
 [4932, 4929, 4925, 2466, 3958, 480, 296, 1, 79132, 3186],
 [4933, 4929, 4925, 1011, 5433, 296, 356, 318, 377, 364],
 [4925, 4929, 4933, 2449, 44225, 296, 480, 356, 2144, 3868],
 [4925, 4929, 4933, 2307, 544, 296, 480, 318, 239, 1093],
 [4936, 4925, 4929, 5845, 1018, 296, 318, 356, 2144, 4085],
 [4925, 4929, 4936, 4210, 5553, 296, 480, 318, 1367, 345],
 [4936, 4925, 4929, 2151, 3616, 480, 296, 1, 5577, 107],
 [4939, 4925, 4936, 869, 3256, 480, 296, 1, 5013, 903],
 [4925, 4936, 4929, 304, 4286, 480, 2858, 1, 161, 280],
 [4941, 4936, 4925, 2176, 547, 480, 296, 318, 913, 1287],
 [4936, 4929, 4925, 2202, 5179, 296, 480, 318, 926, 28],
 [4943, 4925, 4936, 476, 84, 296, 480, 318, 410, 4148],
 [4932, 1885, 83, 2203, 998, 296, 480, 318, 51662, 1251],
 [4932, 4933, 4929, 4210, 463, 1, 296, 480, 2817, 45722],
 [4946, 4933, 4929, 4719, 3553, 296, 377, 367, 30707, 3984],
 [4947, 4933, 4929, 2834, 1410, 296, 356, 318, 1091, 58559],
 [4925, 4933, 4947, 5027, 478, 296, 480, 318, 433, 5618],
 [4925, 4929, 4943, 2426, 4551, 296, 480, 318, 6377, 446],
 [4950, 4933, 4947, 45361, 52604, 296, 480, 318, 2324, 81],
 [4951, 4946, 4933, 1601, 5827, 296, 380, 153, 317, 838],
 [4951, 4947, 4929, 1114, 1869, 480, 296, 318, 3764, 28],
 [4950, 4932, 4933, 3345, 2032, 780, 356, 1, 778, 910],
 [4954, 4925, 4929, 245, 929, 296, 318, 480, 265, 65],
 [4955, 4933, 4951, 278, 5800, 480, 296, 318, 4534, 5618],
 [4956, 4932, 4954, 609, 2032, 296, 380, 318, 3097, 4499],
 [4957, 4956, 4932, 39427, 1034, 296, 480, 318, 1500, 2243],
 [4958, 4947, 4939, 1332, 415, 480, 296, 780, 6264, 1248],
 [4936, 4929, 4943, 1034, 1869, 480, 780, 1, 8376, 1500],
 [4960, 4954, 4956, 1063, 713, 296, 480, 318, 64, 3186],
 [4936, 4941, 4929, 61, 3184, 296, 480, 1, 5502, 1057],
 [4957, 4956, 4932, 4674, 4521, 480, 296, 1, 1347, 3869],
 [4963, 4957, 4956, 713, 2190, 480, 1, 296, 317, 783],
 [4957, 4963, 4956, 3427, 903, 296, 480, 318, 1569, 1231],
 [4933, 4947, 4929, 2386, 779, 296, 356, 480, 6537, 6874],
 [4960, 4954, 4956, 548, 52604, 480, 296, 1, 3863, 81834],
 [4967, 4929, 4936, 2489, 2914, 480, 1, 780, 64, 2186],
 [4957, 4956, 4955, 5067, 2195, 296, 480, 318, 247, 1204],
 [4960, 4954, 4925, 2045, 2077, 296, 480, 318, 2023, 2355],
 [4970, 4951, 4946, 687, 3853, 296, 480, 318, 1274, 466],
 [4971, 4946, 4933, 5642, 31420, 480, 296, 318, 2401, 903],
 [4929, 4954, 4925, 601, 726, 296, 356, 480, 2401, 8972],
 [4973, 4946, 4932, 2769, 929, 296, 480, 318, 40815, 551],
 [4974, 4936, 4941, 1806, 3991, 296, 480, 318, 710, 707],
 [4975, 4946, 4933, 304, 5534, 480, 2858, 1, 2023, 1091],
 [4946, 4933, 4975, 5580, 8783, 296, 377, 367, 2599, 2355],
 [4932, 4970, 4946, 1034, 2769, 480, 296, 1, 613, 1057],
 [4978, 4975, 4946, 297, 254, 296, 318, 480, 3107, 2599],
 [4979, 4936, 4941, 2967, 2554, 296, 480, 318, 1224, 59315],
 [4980, 4975, 4978, 53129, 4177, 296, 377, 356, 3269, 1537],
 [4955, 4951, 4978, 449, 2834, 480, 296, 1, 1293, 8810],
 [4982, 4960, 4954, 241, 27684, 480, 296, 1, 1029, 3107],
 [4957, 4975, 4978, 4286, 984, 296, 356, 480, 784, 4034],
 [4956, 4980, 4975, 2923, 3240, 480, 296, 1, 4534, 2019],
 [4985, 4980, 4933, 266, 1178, 480, 296, 1, 44195, 3054],
 [4925, 4970, 4954, 457, 2182, 296, 480, 318, 44665, 1223],
 [4987, 4975, 4932, 4720, 338, 480, 2858, 1, 265, 56775],
 [4925, 4929, 4951, 255, 5067, 480, 296, 318, 2359, 1914],
 [4989, 4933, 4978, 44399, 828, 296, 480, 318, 8784, 800],
 [4990, 4955, 4950, 2151, 255, 296, 480, 318, 3360, 954],
 [4991, 4980, 4975, 44665, 3370, 296, 380, 377, 3535, 378],
 [4992, 4957, 4991, 8860, 5968, 296, 480, 318, 3764, 4262],
 [4993, 4978, 4975, 2831, 3853, 480, 1, 780, 106100, 1100],
 [4994, 4992, 4963, 287, 2385, 296, 318, 480, 48774, 2422],
 [4995, 4991, 4980, 4595, 4505, 296, 1, 480, 552, 231],
 [4936, 4929, 4925, 2250, 2547, 480, 1, 1198, 1150, 125],
 [4960, 4929, 4970, 4868, 869, 296, 480, 318, 903, 2186],
 [4998, 4992, 4991, 4814, 5960, 296, 480, 1, 194, 3764],
 [4933, 4978, 4951, 586, 3157, 296, 480, 1, 194, 5246],
 [4978, 4955, 4933, 13, 5452, 296, 480, 356, 1150, 2301],
 [4985, 4995, 4980, 4672, 294, 480, 296, 1, 833, 6331],
 [5002, 4936, 4974, 5067, 5857, 480, 296, 1, 538, 1747],
 [5003, 4957, 4998, 4727, 48394, 480, 296, 318, 265, 158],
 [5004, 4975, 4978, 3912, 2190, 780, 260, 1, 1527, 4034],
 [4982, 4954, 4960, 2383, 5642, 296, 480, 318, 6383, 32587],
 [4943, 4936, 4925, 258, 2162, 296, 480, 318, 246, 1954],
 [4925, 4929, 4936, 6793, 8934, 480, 1, 296, 41, 8784],
 [5008, 4929, 4967, 2182, 66, 480, 780, 1, 1175, 2817],
 [5009, 4991, 4951, 4238, 5179, 296, 480, 318, 4270, 2300],
 [5010, 4992, 4995, 2250, 713, 296, 356, 318, 41, 2976],
 [4929, 4947, 4970, 4238, 2183, 480, 780, 1, 750, 567],
 [5012, 4933, 4947, 1538, 44399, 296, 318, 356, 1049, 1251],
 [5013, 4978, 5004, 5845, 1750, 296, 377, 367, 33794, 41566],
 [5014, 4998, 4985, 713, 4606, 480, 1, 2858, 7361, 1091],
 [5015, 4995, 4955, 2559, 2162, 296, 480, 318, 48, 538],
 [5016, 4943, 5002, 4749, 828, 296, 480, 318, 27721, 2843],
 [5017, 4980, 4982, 209, 2684, 480, 296, 318, 3863, 4246],
 [5013, 5004, 4933, 3741, 5442, 1198, 260, 2571, 3698, 2081],
 [4947, 4929, 4936, 4162, 447, 480, 296, 1, 3543, 6365],
 [5020, 4982, 5012, 2095, 609, 1, 296, 356, 446, 4246],
 [5021, 4936, 5002, 2126, 42, 480, 296, 1, 1132, 2817],
 [4960, 4982, 4980, 547, 5593, 296, 480, 318, 688, 2420],
 [5023, 4960, 4982, 548, 3710, 296, 380, 480, 3087, 428],
 [5024, 4980, 4956, 1742, 113453, 296, 480, 318, 1005, 1296],
 [5025, 4933, 4946, 34530, 287, 780, 480, 1, 81562, 2722],
 [5026, 5013, 4978, 4286, 254, 1244, 1188, 14, 1876, 4246],
 [5027, 5021, 4936, 2389, 48780, 296, 480, 1, 3752, 4015],
 [4957, 4992, 4998, 2126, 1744, 480, 780, 1, 647, 3527],
 [5029, 4978, 4995, 238, 586, 296, 1, 780, 8810, 272],
 [5030, 5015, 4991, 2110, 36509, 296, 318, 480, 277, 194],
 [4975, 4980, 4978, 2914, 476, 296, 356, 318, 412, 125],
 [5021, 4936, 4925, 209, 498, 296, 480, 318, 6378, 446],
 [5033, 4951, 4978, 2923, 603, 480, 1, 296, 1552, 5572],
 [5026, 5013, 5012, 573, 2062, 296, 480, 318, 3763, 898],
 [4936, 4967, 5002, 573, 4631, 480, 2858, 1, 616, 969],
 [5036, 4936, 4929, 2831, 209, 480, 2858, 296, 1283, 4447],
 [5012, 4947, 5026, 5027, 3946, 296, 480, 318, 6867, 54001],
 [5038, 5013, 4978, 930, 2389, 377, 296, 367, 1367, 158],
 [5039, 5027, 5036, 2180, 2535, 296, 480, 318, 288, 28],
 [5040, 4985, 5013, 476, 5186, 480, 1, 296, 3869, 3213],
 [5021, 4936, 4979, 4750, 2162, 296, 480, 318, 3745, 458],
 [5021, 5036, 4936, 2210, 5179, 296, 480, 318, 239, 1274],
 [5030, 4992, 4991, 2884, 3240, 296, 480, 356, 6870, 51662],
 [4995, 4992, 4957, 706, 1058, 480, 2858, 1, 168, 4639],
 [5021, 4936, 4967, 4648, 1432, 480, 296, 318, 79132, 4974],
 [5046, 4980, 4991, 930, 159, 296, 356, 377, 50872, 849],
 [5047, 5033, 5038, 1742, 5593, 480, 780, 1, 2324, 3751],
 [5048, 5027, 5039, 81, 1661, 296, 480, 318, 3697, 3980],
 [5049, 4932, 4975, 2184, 36509, 296, 480, 318, 1223, 1093],
 [4954, 4925, 5012, 521, 1608, 296, 480, 318, 446, 5349],
 [5051, 4933, 5026, 2884, 449, 296, 356, 480, 8910, 3793],
 [5012, 5026, 4929, 4505, 5534, 296, 377, 380, 1293, 5377],
 [5053, 4980, 5046, 5857, 4268, 296, 377, 356, 3755, 2987],
 [5054, 5013, 5038, 209, 184, 296, 377, 318, 1275, 30707],
 [5055, 5026, 5013, 1058, 2190, 2571, 260, 1, 2599, 410],
 [5054, 4946, 4975, 1814, 1058, 296, 356, 593, 2599, 3717],
 [4995, 4991, 5053, 54, 2095, 296, 318, 480, 3421, 2019],
 [4995, 4992, 5053, 6464, 641, 1, 780, 296, 1244, 5669],
 [4980, 4975, 5038, 2537, 2152, 296, 356, 367, 6711, 308],
 [5060, 4973, 5053, 1219, 5692, 480, 1, 296, 1377, 849],
 [5061, 5023, 4985, 1174, 2923, 480, 296, 318, 365, 1591],
 [5062, 5013, 4980, 4837, 554, 296, 380, 318, 1231, 2294],
 [5063, 4929, 4946, 478, 2726, 296, 480, 318, 7147, 849],
 [5064, 4955, 5033, 4521, 2190, 296, 480, 318, 32587, 784],
 [5065, 5049, 5063, 431, 81, 296, 480, 318, 1274, 1690],
 [5066, 5055, 5023, 4504, 2385, 296, 480, 1, 969, 707],
 [5067, 4929, 4970, 1610, 2535, 480, 1, 2858, 1593, 1339],
 [5064, 4990, 4958, 2054, 754, 296, 480, 318, 3977, 3671],
 [5012, 5062, 5026, 3994, 1370, 296, 356, 377, 7502, 230],
 [5026, 5013, 5038, 449, 1410, 480, 296, 780, 7361, 1104],
 [4936, 5002, 5036, 27684, 7345, 296, 480, 318, 247, 107],
 [5066, 5054, 5023, 575, 258, 480, 1, 296, 585, 468],
 [4946, 4978, 5026, 4719, 165, 296, 480, 318, 1302, 2406],
 [5053, 5023, 4980, 2037, 5480, 296, 318, 356, 3984, 315],
 [4929, 5012, 4925, 4162, 287, 296, 318, 356, 85, 2702],
 [4957, 4992, 5053, 996, 5893, 296, 356, 1, 1235, 59615],
 [5077, 4963, 4957, 876, 707, 296, 480, 318, 3548, 5747],
 [5026, 4946, 4978, 498, 4549, 2174, 1291, 1101, 11, 539],
 [5012, 5026, 4933, 4650, 2523, 296, 356, 480, 6365, 926],
 [5080, 5026, 5013, 2371, 4663, 296, 380, 377, 1747, 2313],
 [4943, 5048, 4936, 5452, 1750, 296, 480, 318, 592, 277],
 [4995, 5038, 5013, 3568, 447, 153, 292, 296, 4235, 275],
 [5012, 4933, 4925, 44731, 251, 480, 1, 2858, 345, 4973],
 [4925, 4936, 4929, 27005, 8207, 296, 1, 356, 5481, 911],
 [5010, 5077, 4992, 3764, 1608, 296, 480, 356, 41569, 48394],
 [4954, 4925, 5012, 3763, 479, 296, 318, 380, 5349, 5618],
 [4951, 4947, 5051, 2040, 126, 296, 380, 153, 4424, 1100],
 [5064, 5051, 5033, 2953, 609, 480, 296, 1, 14, 2144],
 [4932, 5049, 4987, 2077, 238, 480, 1, 780, 8949, 4865],
 [5012, 4933, 5051, 928, 74458, 296, 1, 780, 2717, 2167],
 [4936, 5021, 4929, 3501, 6834, 480, 296, 318, 292, 39],
 [5092, 5004, 4978, 4620, 913, 296, 1, 480, 85, 3396],
 [5093, 5008, 5067, 6910, 3709, 296, 480, 356, 1377, 2976],
 [5094, 5080, 4951, 996, 2208, 296, 480, 318, 3702, 538],
 [4943, 4925, 4954, 886, 548, 480, 296, 318, 1954, 2414],
 [5096, 5047, 5015, 3401, 5480, 480, 296, 780, 3751, 419],
 [4992, 5010, 4957, 6639, 66, 296, 318, 480, 5246, 28],
 [4974, 5021, 4979, 87, 609, 480, 296, 780, 441, 969],
 [5051, 4958, 4947, 8860, 806, 296, 480, 1, 1194, 3751],
 [5100, 4980, 5014, 278, 1174, 2858, 480, 780, 2492, 6934],
 [4957, 5077, 5003, 586, 2399, 480, 296, 780, 1049, 1175],
 [5102, 5077, 3115, 5433, 2537, 480, 296, 780, 1747, 3863],
 [5103, 5010, 4992, 5362, 1474, 296, 480, 356, 446, 1747],
 [5051, 4933, 5012, 3184, 227, 480, 1, 2858, 209, 858],
 [5105, 4957, 4992, 876, 4354, 296, 480, 318, 616, 1088],
 [5106, 5080, 5038, 601, 498, 296, 380, 153, 3623, 2396],
 [5107, 5060, 5105, 1834, 2726, 296, 480, 318, 2301, 926],
 [5020, 4982, 5023, 6624, 54278, 296, 480, 318, 230, 79132],
 [5100, 5066, 5023, 384, 1610, 480, 296, 1, 412, 144],
 [5110, 4951, 4925, 6955, 4719, 296, 318, 480, 540, 155],
 [5111, 5013, 5054, 631, 2967, 296, 480, 318, 4238, 3984],
 [4947, 5012, 5051, 1427, 2182, 480, 1, 1198, 4975, 2116],
 [5009, 5033, 4951, 3553, 81, 480, 2858, 1, 2401, 1267],
 [4957, 4992, 5105, 415, 2186, 780, 480, 296, 3421, 230],
 [4925, 4943, 4939, 5425, 5208, 480, 780, 1, 2413, 1275],
 [5051, 4989, 4933, 2091, 5452, 296, 780, 480, 1608, 1283],
 [5051, 4978, 4933, 3298, 6795, 480, 1, 780, 1431, 59315],
 [5053, 4980, 4975, 1595, 1015, 296, 1, 480, 3481, 4270],
 [5049, 4932, 4991, 27773, 1370, 480, 2858, 318, 2273, 2712],
 [5120, 4951, 5110, 904, 4629, 480, 780, 1, 30707, 33166],
 [5010, 4956, 5014, 3944, 1600, 480, 780, 1, 3157, 5377],
 [4954, 4960, 5012, 547, 420, 296, 318, 480, 381, 172]]

movies = pd.read_csv('modified_movies2.csv')
movies.drop_duplicates(subset='movieId', inplace=True)


menu = ["Home","Recommendations"]
choice = st.sidebar.selectbox("Menu",menu)

if choice =="Home":
    # LANDING PAGE 
    st.title('Movie Recommender System')
    st.subheader('This is a hybrid recommender system')
    st.text('It is comprised of four models - content based model, clustering model,')
    st.text('Social GCN hybrid Model and a Neural CF model.')
    st.subheader('Hybrid Model - Working')
    st.video("hybrid-model-demo.mp4", format="video/mp4", start_time=0)


if choice =="Recommendations":
    #get recommendations titles
    st.header("Recommendations for a User")
    st.text("The Models have been pre-trained and the results are stored.")
    st.text("Enter a user id and get recommendations for that user.")

    user_id = st.number_input("Enter a user id", min_value=1, max_value=200, value=1, step=1)
    user_id = int(user_id)
    # st.text("The user id entered is {}".format(user_id))
    final_recommendations = weighted[user_id]
    st.subheader("The recommendations for the user are:")
    for id in final_recommendations:
        st.text(movies[movies['movieId']==id]['title'].values[0])




