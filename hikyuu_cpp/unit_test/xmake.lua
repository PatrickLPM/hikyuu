add_requires("doctest")

function coverage_report(target)
    if is_mode("coverage") and not is_plat("windows") and not (linuxos.name() == "ubuntu" and linuxos.version():lt("20.0")) then 
        -- 如需分支覆盖，须在下面 lcov, genhtml 命令后都加入: --rc lcov_branch_coverage=1
        print("Processing coverage info ...")
        
        if not os.isfile("cover-init.info") then
            -- 初始化并创建基准数据文件
            os.run("lcov -c -i -d ./ -o cover-init.info") 
        end

        -- 移除之前的结果，否则容易出错
        os.tryrm('cover.info')
        os.tryrm('cover-total.info')

        -- 收集当前测试文件运行后产生的覆盖率文件
        os.run("lcov -c -d ./ -o cover.info")

        -- 合并基准数据和执行测试文件后生成的覆盖率数据
        os.exec("lcov -a cover-init.info -a cover.info -o cover-total.info")

        -- 删除统计信息中如下的代码或文件，支持正则
        os.run("lcov --remove cover-total.info '*/usr/include/*' \
                '*/usr/lib/*' '*/usr/lib64/*' '*/usr/local/include/*' '*/usr/local/lib/*' '*/usr/local/lib64/*' \
                '*/test/*' '*/.xmake*' '*/boost/*' '*/ffmpeg/*' \
                -o cover-final.info")
        
        -- 生成的html及相关文件的目录名称，--legend 简单的统计信息说明
        os.exec("genhtml -o cover_report --legend --title 'hikyuu'  --prefix=" .. os.projectdir() .. " cover-final.info")

        -- 生成 sonar 可读取报告
        if is_plat("linux") then
            os.run("gcovr -r . -e cpp/test --xml -o coverage.xml")
        end
    end
end

function prepare_run(target)
    local targetname = target:name()
  
    if "unit-test" == targetname or "small-test" == targetname or "prepare-test" == targetname then
      print("copying test_data ...")
      os.rm("$(buildir)/$(mode)/$(plat)/$(arch)/lib/test_data")
      os.cp("$(projectdir)/test_data", "$(buildir)/$(mode)/$(plat)/$(arch)/lib/")
    end
  
    if is_plat("windows") then os.cp("$(env BOOST_LIB)/boost_*.dll", "$(buildir)/$(mode)/$(plat)/$(arch)/lib/") end
  
    -- if is_plat("linux") and os.getenv(BOOST_LIB) > "" then
    --   -- 不确定是否需要加入这段才能在fedora下使用
    --   os.cp("$(env BOOST_LIB)/libboost_*.so.*", "$(buildir)/$(mode)/$(plat)/$(arch)/lib/")
    -- end
  
    if is_plat("macosx") then os.cp("$(env BOOST_LIB)/libboost_*.dylib", "$(buildir)/$(mode)/$(plat)/$(arch)/lib/") end
  end

target("unit-test")
    set_kind("binary")
    set_default(false)

    add_options("hdf5", "mysql", "sqlite", "tdx", "feedback", "stacktrace", "spend_time")

    add_packages("boost", "fmt", "spdlog", "doctest", "sqlite3")
    if get_config("mysql") then
        if is_plat("macosx") then
            add_packages("mysqlclient")
        else
            add_packages("mysql")
        end
    end

    add_includedirs("..")

    if is_plat("windows") then
        add_cxflags("-wd4267", "-wd4996", "-wd4251", "-wd4244", "-wd4805", "-wd4566")
    else
        add_cxflags("-Wno-unused-variable",  "-Wno-missing-braces")
        add_cxflags("-Wno-sign-compare")
    end
    
    if is_plat("windows") and get_config("kind") == "shared" then
        add_defines("HKU_API=__declspec(dllimport)")
    end

    add_deps("hikyuu")

    if is_plat("linux") or is_plat("macosx") then
        add_links("sqlite3")
        add_shflags("-Wl,-rpath=$ORIGIN", "-Wl,-rpath=$ORIGIN/../lib")
    end

    if is_plat("macosx") then
        add_includedirs("/usr/local/opt/mysql-client/include")
        add_linkdirs("/usr/local/opt/mysql-client/lib")
    end

    -- add files
    add_files("**.cpp")

    before_run(prepare_run)
    after_run(coverage_report)
target_end()

target("small-test")
    set_kind("binary")
    set_default(false)
    
    add_options("hdf5", "mysql", "sqlite", "tdx", "feedback", "stacktrace", "spend_time")

    add_packages("boost", "fmt", "spdlog", "doctest", "sqlite3")
    if get_config("mysql") then
        if is_plat("macosx") then
            add_packages("mysqlclient")
        else
            add_packages("mysql")
        end
    end

    add_includedirs("..")

    if is_plat("windows") then
        add_cxflags("-wd4267")
        add_cxflags("-wd4251")
        add_cxflags("-wd4244")
        add_cxflags("-wd4805")
        add_cxflags("-wd4566")
    else
        add_cxflags("-Wno-unused-variable",  "-Wno-missing-braces")
        add_cxflags("-Wno-sign-compare")
    end
    
    if is_plat("windows") and is_mode("release") then
        add_defines("HKU_API=__declspec(dllimport)")
    end

    add_deps("hikyuu")

    if is_plat("linux") or is_plat("macosx") then
        add_shflags("-Wl,-rpath=$ORIGIN", "-Wl,-rpath=$ORIGIN/../lib")
    end

    -- add files
    add_files("./hikyuu/hikyuu/**.cpp");
    add_files("./hikyuu/test_main.cpp")

    before_run(prepare_run)
    after_run(coverage_report)
target_end()
