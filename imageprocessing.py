import os
from keras.preprocessing.image import image,load_img,img_to_array

Class ImageProcessing():
    def __init__(self,folder):
        self.folder = folder
    
    def resize(self,x=32,y=32,c=3,verbose=None):
        self.x = x
        self.y = y
        self.c = c
        os.mkdir(x + "by" + y +"Resized")    
        i = 0
        for im in list:
            #get old name
            name = im.split("/")[-1]
            try:
                #read the image
                z = load_img(im)
                #resize the image
                z = z.resize([self.x,self.y])
                #save the image
                z.save(folder+name)
                i += 1
                if(verbose):
                    if (i %500 == 0 ):
                        print("{} images converted".format(i))
            except:
                print("Cannot process {}".format(name))
        print("Conversion Completed")
        self.z = z 
        
    def imgs_to_array(self,folder,array,verbose=None):
        self.train = image.list_pictures(folder)

        #instatiate the test and train images
        d1 = np.zeros([len(self.train),self.x,self.y,self.c])
        i = 0
        for im in file:
            #read the image
            try:
                z = load_img(im)
                #convert into images and replace in the instatiated datasets above
                list[i] = img_to_array(z)
                i += 1
                if(verbose):
                    if (i%500==0):
                    print("{} images converted".format(i))
            except:
                print("Cannot process image {}".format(im))
        print ("Conversion is Completed")
        return d1
    
    def normalize(self,data,type=1):
        if(type==1):
            d = (data -128)/ 128
        elif(type==2):
            d = data/256
        else:
            d = type(data)
        return d
    
    def to_df(self,data,train = None,id_df,join_on="id"):
        img_id = []
        t = train or self.train
        for dir in t:
            img_id.append(dir.split("/")[-1].split(".")[0])
        img_id_df = pd.Series(id_df,name=join_on)

        #reshape your image and join
        dt1 = d1.reshape([data.shape[0],data.shape[1] * data.shape[2] * data.shape[3]])
        dt_df = pd.DataFrame(dt1)

        del dt1
        del img_id

        #joining the dataframe together 
        dt = dt_df.join(img_id_df)

        del dt_df
        del img_id_df
        gc.collect()
        
        return dt
    
    def merge(self,df,to_csv=False,join_on="id"):
        #merge the two datasets for proper labeling
        final_train_df = df.merge(id_df,on=join_on)
        if(to_csv):
            final_train_df.to_csv("train.csv",index=False)
        return final_train_df
    def finish(self,):
        #converting back to numpy and reshaping
        Xtrain = X_train.values.reshape([len(X_train),self.x,self.y,self.c])
        Xtest = X_test.values.reshape([len(X_test),self.x,self.y,self.c])
        ytrain = y_train.values
        ytest = y_test.values