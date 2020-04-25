import React from "react"
import JSONData from "../../content/output_parsed_file_list.json"

const JSONbuildtime = () => (
  <div>

      <h1>Aerial wallpapers </h1>
      <p>Amazing footage from AppleTV default wallpapers. Mostly drone footage of various cities. Features some satellite footage and underwater footage too! Built from https://github.com/Tawfiqh/aerialWallpapers</p>

      <div className="asset_container" >


          {JSONData.map((data, index) => {

              function assetButtonLink(data, key, title){
                  if(data[key]){
                      return (
                        <>
                          <a href={data[key]}>
                              <span role="img" aria-label="cinema">🎬</span> Watch {title}
                          </a>
                          <br  />
                        </>
                      )
                  }
              }

            return (
            <div className="asset"  key={`asset_${index}`}>
                <h2>{data.accessibilityLabel} <em>{data.id}</em></h2>
                <p>
                    <img src={"thumbnails/" +data.id +".jpeg"} alt={data.accessibilityLabel} title={data.accessibilityLabel} />
                </p>

                <div className="button_container" >
                    <p>
                    {assetButtonLink(data, "url", "")}
                    {assetButtonLink(data, "url-1080-SDR", "1080p")}
                    {assetButtonLink(data, "url-4K-SDR", <em>4K</em>)}
                    {assetButtonLink(data, "url-1080-H264", "1080p-H264")}
                    </p>


                    {(data["url-1080-HDR"] || data["url-4K-HDR"]) && <h4>HDR</h4>}
                    <p>
                    {assetButtonLink(data, "url-1080-HDR", "1080-HDR")}
                    {assetButtonLink(data, "url-4K-HDR", "4K-HDR ")}
                </p>
                </div>
            </div>
            )
          })}

      </div>



  </div>
)
export default JSONbuildtime
