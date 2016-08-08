import java.util.ArrayList;
import com.unh.unhcfreg.RapidAndroidParser;
import com.unh.unhcfreg.QueryBlock;
import dataComponent.MethodElement;

public class APIParser {
	public static void main(String args[]){
		
		final RapidAndroidParser rapid = new RapidAndroidParser();
		String apk = args[0]; 
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