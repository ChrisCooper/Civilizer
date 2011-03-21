function showNodes() {
  
    var point_parent = document.documentElement;
  
    var textblock = document.createElement("p");
    var text = document.createTextNode("<div class="point" id="point_762948">
		<div class="point_controls" id="point_controls_762948">
		    <div class="vote_up_off"></div>
		    <div class="vote_count">523</div>
		    <div class="vote_down_off"></div>
		</div>
		<div class="point_text" id="point_text_762948">
		    <div class="point_info" id="point_info_762948">
			<span class="point_username" id="point_user_16571623">
			    AwesomeUser123
			</span>
			<span class="point_votes" id="point_votes_762948">
			    (+6563/-2352)
			</span>
		    </div>
		    <div class="point_contents" id="point_contents_762948">
			I just love writing insightful points everywhere! This is a really long comment that must go into extreme depth on some particular issue. Hopefully it is the issue that is meant to be discussed in this article, but I guess good discussion is good discussion regardless of where it occurs. Maybe we can migrate it!
		    </div>
		</div>
	    </div>")
    textblock.appendChild(text)
    document.body.appendChild(textblock)
}