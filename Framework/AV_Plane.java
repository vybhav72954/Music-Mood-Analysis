
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

import javax.media.*;
import javax.media.rtp.*;
import javax.media.rtp.event.*;
import javax.media.rtp.rtcp.*;
import javax.media.protocol.*;
import javax.media.protocol.DataSource;
import javax.media.format.AudioFormat;
import javax.media.format.VideoFormat;
import javax.media.Format;
import javax.media.format.FormatChangeEvent;
import javax.media.control.BufferControl;

public class AnnoEmo extends JFrame implements CommonValue{

	
	AVplane 	avp;
	UserDataFrame 	userDataF;
	
	
  	Player		jmfPlayer;
  	SongPanel[] 	songPanels;
  	boolean 	isplaying = false;
  	int 		playingID = -1;
  	
  	int 		nSong;

  	
  
  	public AnnoEmo() {
  		
  		
  		super("AnnoEmo");
  		setSize(400,700);
  		setLocation(2);
  		setClose();
  		
  		
  		// load songs
  		File directory = new File(DATABASE+"\\");
		File[] fs = directory.listFiles();
		nSong = fs.length;
  		
  		
  		// init song list
  		JPanel content = new JPanel();
  		content.setLayout(new GridLayout(nSong,1));
  		
  		songPanels = new SongPanel[nSong];
  		for(int i=0; i<nSong; ++i) {
  			songPanels[i] = new SongPanel(fs[i].getAbsolutePath(),fs[i].getName()+"-"+(i+1),"tmp",this,i+1);
  			//System.err.println(fs[i].getName());
    			content.add(songPanels[i]);
    		}

	    	JScrollPane scroll = new JScrollPane(content);
  		add(scroll);
  		
  		
  		// init AVplane
  		avp = new AVplane(this,nSong);
  		avp.setLocation(8);
				
  		avp.getFrame().setVisible(false);
  		this.setVisible(false);		// will be visible after UserDataFrame ends


		// init UserDataFrame
		userDataF = new UserDataFrame(this);
		
  	}
  	
  	public void startExperiment(String s) {	
  		// AnnoEmo and AVplane show up
  		
  		avp.setFileWriter(s);
  		avp.getFrame().setVisible(true);
  		this.setVisible(true);
  		
  	}
  	
  	
  	public void enableASongPanel(int i) {
  		// enable song panels one by one
  		
  		if(i<nSong) {
  			if(i>0) songPanels[i-1].setColor(Color.ORANGE);
    				songPanels[i].setEnabled(true);
    		}
  	}
  	
  	
  	public void enableAllSongPanels() {
  		for(int i=0; i<nSong; ++i) {
    			songPanels[i].setEnabled(true);
    		}	
  	}
  	
  	
  	public void stopPlay() {
  		if(playingID!=-1) songPanels[playingID].stop();
  	}
  	
  	
  	public void setPlayingID(int id)
  	{
  		if(playingID!=-1 & playingID!=id)
  			stopPlay();
  		
  		if(avp.playingID!=-1)
  			avp.stopPlay();
  		
  		if(playingID!=-1)  songPanels[playingID].changeColor();  
  		if(id<nSong) songPanels[id].setPlayingColor();
  		playingID = id;	
  		
  		avp.add_song(id,songPanels[playingID].musicName,songPanels[playingID].musicPath);
  	}
  	
  	public int getPlayingID() { return playingID; }


	public void setLocation(int place) {
		
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		Dimension frameSize = getSize();
		int x = (screenSize.width - frameSize.width);
		int y = (screenSize.height - frameSize.height);
		
		if(place==1) 		setLocation(10, 0);	// left+up
		else if(place==2) 	setLocation(10, y/2);	// left+center
		else if(place==3) 	setLocation(10, y);	// left+down
		else if(place==4) 	setLocation(x/2, 0);	// center+up
		else if(place==5) 	setLocation(x/2, y/2);	// center+center
		else if(place==6) 	setLocation(x/2, y);	// center+down
		else if(place==4) 	setLocation(x-10, 0);	// right+up
		else if(place==5) 	setLocation(x-10, y/2);	// right+center
		else if(place==6) 	setLocation(x-10, y);	// right+down
  	}
  	
  	
  	public void setClose() {
  		addWindowListener(new WindowAdapter() {
		public void windowClosing(WindowEvent e) {
			try {
		  		if (jmfPlayer!=null) {
			      		jmfPlayer.stop(); System.err.println("stoped");
			      		jmfPlayer.close(); System.err.println("closed");
			      		jmfPlayer=null;
		    		}
		    	} catch(Exception ex) {
		  		ex.printStackTrace();	
		  	}
		    	dispose();
		}});
	}
  
  
  	public static void main(String[] args) {
  	  	
  		AnnoEmo AnnoEmoer = new AnnoEmo();
  		
  	}  	
  
}
