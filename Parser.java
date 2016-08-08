import java.util.ArrayList;
import com.unh.unhcfreg.RapidAndroidParser;
import com.unh.unhcfreg.QueryBlock;
import dataComponent.MethodElement;
import dataComponent.StringElement;
import java.util.concurrent.ExecutorService;  
import java.util.concurrent.Executors; 
import java.io.File;
import java.io.*;

public class Parser {  
     public static void main(String[] args) {  

     	//ArrayList<String> apkList = new ArrayList<String>();
     	//apkList = walkin(new File("/home/openandroid/Documents/apks"));

     	fileIO f = new fileIO();
     	f.walkin(new File("/home/openandroid/Documents/apks"));
     	ArrayList<String> apkList = f.getList();
     	ExecutorService executor = Executors.newFixedThreadPool(2);
     	for(String apk: apkList){
     		Runnable worker = new stringWorkerThread(apk);  
            executor.execute(worker);//calling execute method of ExecutorService 
     	}
     	executor.shutdown();  
        while (!executor.isTerminated()) {   }  
  		
        System.out.println("Finished all threads");
        /*ExecutorService executor = Executors.newFixedThreadPool(5);//creating a pool of 5 threads  
        for (int i = 0; i < 10; i++) {  
            Runnable worker = new WorkerThread("" + i);  
            executor.execute(worker);//calling execute method of ExecutorService  
          }  
        executor.shutdown();  
        while (!executor.isTerminated()) {   }  
  
        System.out.println("Finished all threads");*/
    }

private static class fileIO {

	private ArrayList<String> apkList = new ArrayList<String>();

	public fileIO(){}

	private void walkin(File dir) {
        String pattern = ".apk";
        File listFile[] = dir.listFiles();
        if (listFile != null) {
            for (int i=0; i<listFile.length; i++) {
                if (listFile[i].isDirectory()) {
                    walkin(listFile[i]);
                } else {
                    if (listFile[i].getName().endsWith(pattern)) {
                        this.apkList.add(listFile[i].getPath());
                    }
                }
            }
        }
    }

    public ArrayList<String> getList(){ return this.apkList; }
}  

}  

class stringWorkerThread implements Runnable {  
    private String apk;
    private String decode = "/home/openandroid/Documents/solr_json/"; 
    public stringWorkerThread(String s){  
        this.apk=s;
    }  
     public void run() {  
        //System.out.println(Thread.currentThread().getName()+" (Start) message = "+apk);  
        //ArrayList<String> strs = new ArrayList<String>();
        //strs = 
        process();//call processmessage method that sleeps the thread for 2 seconds
        String dir = decodeDir();
        toFile(dir);

        //System.out.println(Thread.currentThread().getName()+" (End)");//prints thread name  
    }  
    private void process() {  

    	final RapidAndroidParser rapid = new RapidAndroidParser();
			//String apk = "/home/openandroid/Documents/apks/malware/fff29f78324c75c8727426d77b128d3ee9df7ba6a1f0be1617be3430ed99d050.apk"; 
			ArrayList<String> temp = new ArrayList<String>();
			rapid.setSingleApk(this.apk);

		 	rapid.setQuery(new QueryBlock(){
		 
				public void queries() {
					//print sting list
					ArrayList<StringElement>stringList=rapid.getStringList();
					for(int i = 0; i< stringList.size(); i ++){
					//temp.add(stringList.get(i).stringContent)
					System.out.println(""+stringList.get(i).stringContent);
					}
				}
			});

        //try {  Thread.sleep(2000);  } catch (InterruptedException e) { e.printStackTrace(); }  
    }

    private void toFile(String dir){

    }  

    private String decodeDir(){
    	String[] fileNames = this.apk.split("/");
    	String apkName = fileNames[fileNames.length-1];
    	apkName = apkName.replaceAll(".apk", "");
    	String decodeDir = this.decode + apkName + ".json";
    	return decodeDir;
    }
}  

class StringThread extends Thread {
	public void run() {

			final RapidAndroidParser rapid = new RapidAndroidParser();
			String apk = "/home/openandroid/Documents/apks/malware/fff29f78324c75c8727426d77b128d3ee9df7ba6a1f0be1617be3430ed99d050.apk"; 
			rapid.setSingleApk(apk);
		 	rapid.setQuery(new QueryBlock(){
		 
				public void queries() {
					//print sting list
					ArrayList<StringElement>stringList=rapid.getStringList();
					for(int i = 0; i< stringList.size(); i ++){
					System.out.println(""+stringList.get(i).stringContent);
					}
				}
			});
		
		}
}

class APIThread extends Thread {
	public void run() {

			final RapidAndroidParser rapid = new RapidAndroidParser();
			String apk = "/home/openandroid/Documents/apks/malware/fff29f78324c75c8727426d77b128d3ee9df7ba6a1f0be1617be3430ed99d050.apk"; 
			rapid.setSingleApk(apk);
		 	rapid.setQuery(new QueryBlock(){
		 
				public void queries() {
				// print API list
				ArrayList<MethodElement>apiList=rapid.getApiList();
				for(int j = 0; j<apiList.size(); j++){
					apiList.get(j).printFields();
				}
				}
			});

				
		}
}
