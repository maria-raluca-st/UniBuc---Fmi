public class GenreFactory {
	
    //use getGenre method to get object of type genre 
    public Genre getGenre(String genreType)
    {
       if(genreType == null)
       {
          return null;
       }		
       if(genreType.equalsIgnoreCase("Rock"))
       {
          return new Rock();
       } 
       else if(genreType.equalsIgnoreCase("Jazz"))
       {
          return new Jazz();
          
       } 
       else if(genreType.equalsIgnoreCase("Classical"))
       {
          return new Classical();
       }
       
       return null;
    }
 }